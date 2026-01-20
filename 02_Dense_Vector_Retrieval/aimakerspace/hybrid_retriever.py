import numpy as np
from typing import List, Tuple, Dict
from rank_bm25 import BM25Okapi
from aimakerspace.vectordatabase import VectorDatabase


class HybridRetriever:
    """
    Combines dense vector search (semantic) with sparse BM25 search (keyword-based)
    for improved retrieval quality.
    """
    
    def __init__(self, vector_db: VectorDatabase, alpha: float = 0.5):
        """
        Initialize hybrid retriever.
        
        Args:
            vector_db: VectorDatabase instance with embedded documents
            alpha: Weight for combining scores (0-1). 
                   0 = pure BM25, 1 = pure vector search, 0.5 = equal weight
        """
        self.vector_db = vector_db
        self.alpha = alpha
        
        # Extract documents and build BM25 index
        self.documents = list(vector_db.vectors.keys())
        self.tokenized_docs = [doc.lower().split() for doc in self.documents]
        self.bm25 = BM25Okapi(self.tokenized_docs)
        
    def search(self, query: str, k: int = 4) -> List[Tuple[str, float]]:
        """
        Perform hybrid search combining BM25 and vector similarity.
        
        Args:
            query: Search query
            k: Number of results to return
            
        Returns:
            List of (document, combined_score) tuples
        """
        # Get BM25 scores
        tokenized_query = query.lower().split()
        bm25_scores = self.bm25.get_scores(tokenized_query)
        
        # Normalize BM25 scores to [0, 1]
        max_bm25 = max(bm25_scores) if max(bm25_scores) > 0 else 1
        normalized_bm25 = {doc: score / max_bm25 
                          for doc, score in zip(self.documents, bm25_scores)}
        
        # Get vector similarity scores
        vector_results = self.vector_db.search_by_text(query, k=len(self.documents))
        normalized_vector = {doc: score for doc, score in vector_results}
        
        # Combine scores
        combined_scores = []
        for doc in self.documents:
            bm25_score = normalized_bm25.get(doc, 0)
            vector_score = normalized_vector.get(doc, 0)
            
            # Weighted combination
            combined_score = (1 - self.alpha) * bm25_score + self.alpha * vector_score
            combined_scores.append((doc, combined_score))
        
        # Sort by combined score and return top k
        combined_scores.sort(key=lambda x: x[1], reverse=True)
        return combined_scores[:k]
    
    def explain_scores(self, query: str, k: int = 4) -> Dict:
        """
        Return detailed scoring breakdown for debugging/transparency.
        
        Args:
            query: Search query
            k: Number of results to analyze
            
        Returns:
            Dictionary with BM25, vector, and combined scores
        """
        tokenized_query = query.lower().split()
        bm25_scores = self.bm25.get_scores(tokenized_query)
        
        max_bm25 = max(bm25_scores) if max(bm25_scores) > 0 else 1
        normalized_bm25 = {doc: score / max_bm25 
                          for doc, score in zip(self.documents, bm25_scores)}
        
        vector_results = self.vector_db.search_by_text(query, k=len(self.documents))
        normalized_vector = {doc: score for doc, score in vector_results}
        
        results = []
        for doc in self.documents:
            bm25_score = normalized_bm25.get(doc, 0)
            vector_score = normalized_vector.get(doc, 0)
            combined_score = (1 - self.alpha) * bm25_score + self.alpha * vector_score
            
            results.append({
                'document': doc[:100] + '...' if len(doc) > 100 else doc,
                'bm25_score': bm25_score,
                'vector_score': vector_score,
                'combined_score': combined_score
            })
        
        results.sort(key=lambda x: x['combined_score'], reverse=True)
        return {
            'query': query,
            'alpha': self.alpha,
            'top_results': results[:k]
        }
