# SafeSpace Events: AI-Powered Community Event Discovery

**Working Title:** SafeSpace Events: AI-Powered Community Event Discovery with Values-Based Filtering  
**Alternative Names:** EventMatch AI, Community Compass

## Project Overview

An agentic system that searches the internet for community events in a specified city, filtered by user-defined values-based criteria (e.g., free, alcohol-free, secular, apolitical, safe), and returns a categorized list of matching events.

---

## Problem Statement

**1-Sentence Description:**  
Finding community events that match personal values and safety criteria requires manually searching across fragmented platforms and vetting dozens of listings, turning what should be a 5-minute task into an hour-long research project.

### Why This Matters

**For the User:**
The target user—parents, individuals in recovery, people seeking secular/apolitical spaces, or newcomers to a city—faces a compounding accessibility barrier. Event platforms like Eventbrite and Meetup optimize for volume, not values alignment. A "free community gathering" might be a church recruitment event. A "networking mixer" might center around a bar. A "family festival" might have political sponsors. Users must click through 20-30 listings, read fine print, check venue websites, and cross-reference reviews just to find 2-3 suitable options. This friction doesn't just waste time—it actively discourages community participation. Research shows that decision fatigue reduces follow-through; when finding an event feels like work, people simply stay home.

For newcomers to a city, this problem compounds isolation. They lack local knowledge about which venues are truly family-friendly or which organizations have hidden agendas. The stakes are higher too—attending an incompatible event wastes limited social energy and creates negative first impressions of a new community. Current solutions (Facebook Events, Google search, word-of-mouth) require either algorithm manipulation by advertisers, keyword guessing, or an established social network—none of which serve the "new in town, looking for safe community entry points" user effectively.

**For the Company/World:**
This addresses the "paradox of choice" in modern urban living - we have access to thousands of events but lack tools to find the right ones efficiently. By reducing barriers to community engagement, this tool can increase social connection, reduce isolation, and make cities more accessible to diverse populations.

---

## Success Criteria

**Definition of Success:**  
Users find 3-5 relevant events in under 2 minutes, versus 30+ minutes of manual searching.

**Key Performance Indicator (KPI):**  
User saves the output and attends at least one event within 7 days (measured via follow-up survey).

**Additional Metrics:**
- Search-to-save conversion rate
- Filter accuracy (user ratings of event matches)
- Time saved per search
- Repeat usage rate

---

## Target Audience

**Primary Users:**
- Parents seeking family-friendly activities
- Individuals in recovery avoiding alcohol-centric events
- People of non-dominant cultural backgrounds seeking inclusive spaces
- Professionals new to a city wanting safe community entry points

**User Pain Points:**
- Time waste (30+ minutes per search)
- Safety concerns (unknown venues/organizations)
- Repeated disappointment from events that looked good online but violated their values in practice
- Lack of local knowledge about which events/venues are truly compatible
- Decision fatigue from too many options without meaningful filtering

---

## Proposed Solution

### User Experience

The user opens a clean web interface and inputs their city plus 3-5 values-based filters via checkboxes and text (e.g., "San Francisco," "free," "no alcohol," "family-friendly," "secular"). They click "Find Events" and within 30-60 seconds receive a categorized list organized by activity type:

- **Outdoor/Active** (3 hiking groups, 2 bike rides)
- **Arts & Culture** (library reading, museum free day)
- **Learning** (coding workshop, language exchange)
- **Social** (board game cafe meetup)

Each event shows:
- Confidence score
- Brief description
- Date/time
- One-line explanation of why it matches criteria (e.g., "Venue is a public library - alcohol-free, non-religious setting")

**Key Features:**
- "Save Preferences" button stores user filters in memory for one-click future searches
- Export results as calendar files (.ics)
- Shareable links for results
- Feedback loop where users rate event matches to improve filtering accuracy

The entire experience feels like having a knowledgeable local friend who pre-vetted everything—trustworthy, fast, and genuinely helpful rather than algorithmically manipulative.

---

## Technical Architecture

### High-Level System Design

```
User Query (San Francisco, free, safe, no alcohol/religion/politics)
           ↓
[Supervisor Agent] - Breaks down search into parallel tasks
           ↓
    ┌──────┴──────┬──────────┬──────────┐
    ↓             ↓          ↓          ↓
[Researcher 1] [Researcher 2] [Researcher 3] [Researcher 4]
Eventbrite     Meetup.com     Local sites   Social media
           ↓
[Filter Agent] - Applies criteria (free, safe, no alcohol, etc.)
           ↓
[Categorization Agent] - Groups by activity type
           ↓
[Final Compilation] - Structured output with categories
```

### Core Components

#### 1. Supervisor Agent
- **Role:** Decomposes user query into multiple targeted search queries
- **Pattern:** Supervisor-Researcher delegation (from Notebook 08)
- **Model:** GPT-4 or Claude Sonnet for reasoning
- **Responsibilities:**
  - Analyze user intent and filters
  - Generate 4-5 parallel search queries for different platforms
  - Coordinate researcher agents
  - Aggregate results

#### 2. Parallel Researcher Agents (4-5 agents)
- **Role:** Execute searches on different platforms simultaneously
- **Pattern:** Multi-agent with parallel execution (from Notebook 05)
- **Tool:** Tavily Search API
- **Targets:**
  - Eventbrite
  - Meetup.com
  - Local city event calendars
  - Community boards
  - Social media event pages
- **Output:** Raw event listings with descriptions

#### 3. Filter Agent
- **Role:** Evaluate events against user criteria
- **Pattern:** ReAct agent with reasoning (from Notebook 03)
- **Core Innovation:** Uses LLM reasoning for values-based filtering
- **Capabilities:**
  - Detect implicit alcohol presence ("wine included" buried in text)
  - Identify political framing in descriptions
  - Recognize religious context
  - Assess safety indicators
  - Evaluate cost (truly free vs. suggested donation)
- **Output:** Filtered event list with confidence scores

#### 4. Categorization Agent
- **Role:** Semantically group events by activity type
- **Pattern:** Semantic understanding with structured outputs
- **Capabilities:**
  - Understand "trail cleanup" and "park yoga" both belong in "Outdoor/Active"
  - Create dynamic categories based on results
  - Handle edge cases (e.g., "museum lecture" could be Arts OR Learning)
- **Output:** Categorized event dictionary

#### 5. Memory System
- **Role:** Store user preferences for repeat usage
- **Pattern:** Long-term memory with namespaces (from Notebook 06)
- **Storage:**
  - User filter preferences
  - Past successful matches
  - Venue characteristics (e.g., "The Mill is a coffee shop, typically alcohol-free")
- **Implementation:** LangGraph InMemoryStore with user_id namespaces

### Architecture Pattern: Supervisor-Researcher Delegation

This project directly maps to the **Open Deep Research** pattern from Week 8:

```python
# Hierarchical State Structure
AgentState (Top Level)
  - messages: conversation history
  - user_filters: dict of criteria
  - raw_events: accumulated from researchers
  - filtered_events: after filtering
  - categorized_events: final output

SupervisorState (Middle Level)
  - research_iterations: count of delegations
  - researcher_outputs: results from parallel agents

ResearcherState (Bottom Level)
  - platform: which site to search
  - query: search string
  - results: scraped events
```

### Search Strategy

**Recommended Approach:** Start broad, then filter

1. Initial search: "free events [city_name]"
2. Let researcher agents query multiple platforms in parallel
3. Use Filter Agent to apply nuanced criteria
4. Reason: LLMs excel at understanding context and subtext that keyword searches miss

**Alternative:** Include all filters in initial search
- Pro: Fewer results to process
- Con: Might miss events with poor metadata but good actual content

---

## Technical Stack

### Core Framework
- **LangGraph:** Workflow orchestration, state management
- **LangChain:** LLM integrations, tool interfaces

### Models
- **Primary LLM:** 
  - Anthropic Claude Sonnet 4 (supervisor, filtering reasoning)
  - Or OpenAI GPT-4 (alternative)
- **Specialist LLM:**
  - OpenAI GPT-4o-mini (researcher agents, cost-effective)
- **Embeddings (optional for semantic memory):**
  - OpenAI text-embedding-3-small

### Tools & APIs
- **Tavily Search API:** Web search for events
- **Alternative:** Anthropic native web search (if available)

### Storage
- **Short-term:** LangGraph MemorySaver with thread_id
- **Long-term:** InMemoryStore with namespaces
- **Optional:** Qdrant for semantic venue/event knowledge base

### Deployment
- **Frontend:** Streamlit or Gradio for demo
- **Backend:** Python with LangGraph
- **Hosting:** Local for demo, consider LangGraph Cloud for production

---

## Implementation Roadmap

### Phase 1: MVP (Demo Scope)
**Goal:** Prove the concept with core functionality

- [ ] Supervisor agent that decomposes city query
- [ ] 2-3 parallel researcher agents with Tavily search
- [ ] Basic filter agent (free, alcohol presence)
- [ ] Simple categorization (2-3 categories)
- [ ] Streamlit interface for input/output
- [ ] Test with 1-2 cities (San Francisco, Austin)

**Estimated Complexity:** 2-3 days of focused development

### Phase 2: Enhanced Filtering
**Goal:** Add sophisticated values-based filtering

- [ ] Expand filter agent reasoning (religion, politics, safety)
- [ ] Confidence scoring system
- [ ] Edge case handling
- [ ] User feedback loop for accuracy

### Phase 3: Memory & Personalization
**Goal:** Make it useful for repeat users

- [ ] User preference storage
- [ ] One-click repeat searches
- [ ] Venue knowledge base (RAG component)
- [ ] Learning from user ratings

### Phase 4: Production Ready
**Goal:** Deploy as a real application

- [ ] Error handling and retries
- [ ] Rate limiting and caching
- [ ] Multiple city support
- [ ] Calendar export (.ics files)
- [ ] Shareable result links
- [ ] Analytics dashboard

---

## Key Technical Concepts (from AIE9 Course)

### Notebook 03: The Agent Loop
- **ReAct Pattern:** Think → Act → Observe loop
- **Application:** Filter agent reasoning about event compatibility
- **Key Learning:** Agents can reason about ambiguous criteria

### Notebook 04: Agentic RAG
- **Pattern:** Retrieval-Augmented Generation
- **Application:** Venue knowledge base for context
- **Key Learning:** Combine search with semantic understanding

### Notebook 05: Multi-Agent with LangGraph
- **Pattern:** Supervisor orchestration, parallel execution
- **Application:** Multiple researcher agents searching simultaneously
- **Key Learning:** Agent teams outperform single agents for decomposable tasks

### Notebook 06: Agent Memory
- **Pattern:** Short-term (checkpointer) + Long-term (store)
- **Application:** User preference storage, venue characteristics
- **Key Learning:** Memory makes agents personalized and efficient

### Notebook 07: Deep Agents
- **Pattern:** Planning, context management, subagent spawning
- **Application:** Complex filtering logic, dynamic categorization
- **Key Learning:** Long-horizon tasks need explicit planning

### Notebook 08: Open Deep Research
- **Pattern:** Supervisor-researcher delegation, parallel research
- **Application:** DIRECT TEMPLATE for this project
- **Key Learning:** Hierarchical delegation scales to complex information gathering

---

## Data Sources

### Primary Targets
1. **Eventbrite:** Largest event platform
2. **Meetup.com:** Community-focused events
3. **Local city calendars:** City-specific events
4. **Facebook Events:** Social event discovery
5. **Community boards:** Neighborhood-specific listings

### Search Approach
- Use Tavily API to query these platforms
- Tavily handles web scraping, returns structured results
- Focus on event description text for LLM analysis

---

## Example User Flow

### Input
```
City: San Francisco
Filters:
  - Free: Yes
  - Alcohol: No
  - Religion: No
  - Politics: No
  - Safety: Family-friendly
```

### Output
```
🎯 Found 12 events matching your criteria

📚 LEARNING & CULTURE (4 events)
  ✓ Library Book Club - Mission Branch
    📅 Thu Feb 13, 6:00 PM | Free
    💯 95% match - Public library, no alcohol, secular setting
    
  ✓ Museum Free Thursday - de Young Museum
    📅 Thu Feb 13, All day | Free
    💯 92% match - Family-friendly, educational focus

🏃 OUTDOOR & ACTIVE (5 events)
  ✓ Golden Gate Park Group Hike
    📅 Sat Feb 15, 9:00 AM | Free
    💯 98% match - Public park, volunteer-led, all ages welcome
    
  ✓ Community Garden Work Day
    📅 Sat Feb 15, 10:00 AM | Free
    💯 90% match - Neighborhood garden, family-oriented

🎨 ARTS & CREATIVE (3 events)
  ✓ Free Drawing Class - Community Center
    📅 Sun Feb 16, 2:00 PM | Free
    💯 88% match - City-run program, all ages

[Export Calendar] [Share Results] [Save Preferences]
```

---

## Open Questions for Development

### Scope Decisions
1. **City Coverage vs. Filter Depth:** Should MVP focus on comprehensive city coverage (fewer filter options) or deep filtering accuracy (fewer cities)?
   - **Recommendation:** Start with 2-3 cities, deep filtering accuracy for demo impact

2. **Category Breadth:** How many event categories to support initially?
   - **Recommendation:** 3-5 categories for MVP (Outdoor, Learning, Social, Arts, Food)

### Technical Decisions
3. **Tavily Rate Limits:** Is Tavily's free tier sufficient for parallel agent searches?
   - **Investigation needed:** Test 4-5 simultaneous searches
   - **Backup plan:** Implement caching for frequently searched cities

4. **Filtering Strategy:** Broad search + LLM filter OR narrow search from the start?
   - **Recommendation:** Broad search + filter (leverages LLM reasoning strength)

5. **Deployment Platform:** Streamlit vs. Gradio vs. custom web app?
   - **For Demo:** Streamlit (faster, good enough)
   - **For Production:** Custom React + FastAPI backend

### Context Engineering
6. **Prompt Optimization:** How to calibrate "safety" and "family-friendly" filtering?
   - **Approach:** Few-shot examples in system prompts
   - **Testing:** Manual evaluation with 20-30 edge cases

7. **Confidence Scoring:** How to calculate match confidence?
   - **Factors:** 
     - Direct filter matches (free, no alcohol)
     - Implicit indicators (venue type, organizer)
     - Description sentiment/tone
     - Historical accuracy (if memory is available)

---

## Success Metrics for Demo

### Qualitative
- [ ] System finds events that manual search would miss
- [ ] Filtering accurately catches subtle exclusion criteria
- [ ] Categorization makes semantic sense
- [ ] UI feels intuitive and trustworthy

### Quantitative
- [ ] Returns 5-15 events per search
- [ ] <60 second total execution time
- [ ] >80% accuracy on manual filter validation
- [ ] 3-5 meaningful categories per result set

### Demonstration Flow
1. Show San Francisco search with strict filters
2. Highlight an event caught by LLM reasoning (e.g., detected hidden alcohol)
3. Compare to raw Eventbrite search results
4. Show Austin search with different filters to prove generalization
5. Demonstrate "Save Preferences" → instant second search

---

## References & Resources

### Course Materials
- **AIE9/03_The_Agent_Loop:** ReAct pattern fundamentals
- **AIE9/04_Agentic_RAG_From_Scratch:** RAG for knowledge retrieval
- **AIE9/05_Multi_Agent_with_LangGraph:** Multi-agent orchestration
- **AIE9/06_Agent_Memory:** Memory systems implementation
- **AIE9/07_Deep_Agents:** Planning and context management
- **AIE9/08_Open_DeepResearch:** Supervisor-researcher pattern (PRIMARY TEMPLATE)

### External Documentation
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Tavily API Docs](https://docs.tavily.com/)
- [LangChain Multi-Agent Patterns](https://python.langchain.com/docs/tutorials/agents/)

### Architecture Patterns
- **Supervisor Pattern:** Central orchestrator delegates to specialists
- **Hierarchical Delegation:** Supervisors manage teams of agents
- **Parallel Execution:** Multiple agents work simultaneously
- **Context Engineering:** Treat context window as prime real estate (Dex Horthy, 12-Factor Agents)

---

## Notes & Considerations

### Why This Project is Well-Suited to AIE9 Skills
1. **Direct Pattern Match:** Supervisor-researcher from Week 8 maps 1:1 to event discovery
2. **Multi-Modal Agents:** Different agents for search, filter, categorize
3. **Real-World Search:** Tavily integration proven in course materials
4. **Values-Based Filtering:** Showcases LLM reasoning superiority over keyword matching
5. **Practical ROI:** Clear time savings, relatable problem for stakeholders
6. **Scalable:** Works for any city, extensible to more filters

### Potential Challenges
1. **Search Result Quality:** Event platforms may have inconsistent metadata
   - **Mitigation:** Use LLM to parse unstructured descriptions
2. **False Positives:** Filter might miss subtle exclusion criteria
   - **Mitigation:** Confidence scores + user feedback loop
3. **Rate Limits:** Parallel searches might hit Tavily limits
   - **Mitigation:** Caching, staged rollout
4. **Categorization Ambiguity:** Some events fit multiple categories
   - **Mitigation:** Allow multi-category assignment or "Best Fit" logic

### Future Enhancements
- **Location-Based Filtering:** Events within X miles of user
- **Time-Based Filtering:** This weekend, next month, etc.
- **Accessibility Filters:** Wheelchair accessible, ASL interpretation
- **Social Features:** Share with friends, RSVP tracking
- **Mobile App:** Native iOS/Android experience
- **Email Digests:** Weekly curated event lists

---

## Contact & Collaboration

**Project Author:** James Damante  
**Course:** AI Makerspace AIE9 - Production AI Engineering  
**Timeline:** February 2026  
**Status:** Planning phase for cohort final project

---

## License & Usage

This project is being developed as part of the AI Makerspace AIE9 certification program. 

**Intended Use:** Educational demonstration of production-ready agentic systems with real-world applicability.

---

*Last Updated: February 9, 2026*
