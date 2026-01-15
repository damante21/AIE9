<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE9/tree/main/00_AIE_Quicklinks)

| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Vibe Check!](../00_Docs/Session_Sheets/01_Vibe_Check.md) |[Recording!](https://drive.google.com/file/d/1Rsmm0Hld3WFHRxhZpEDLN_JREQ43yhwu/view?usp=drive_link) | [Session 1 Slides](https://www.canva.com/design/DAG-EBzN2PQ/gE9-Uma217yych4M7GCjSw/edit?utm_content=DAG-EBzN2PQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 1 Assignment: Vibe Check](https://forms.gle/NeN59bCLdtXvwzVJ9) | [Feedback 1/13](https://forms.gle/1im4nmYK9cW9MFEk6) |

## 🏗️ How AIM Does Assignments

> 📅 **Assignments will always be released to students as live class begins.** We will never release assignments early.

Each assignment will have a few of the following categories of exercises:

- ❓ **Questions** – these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion in your breakout rooms!

- 🏗️ **Activities** – these will be work or coding activities meant to reinforce specific concepts or theory components.

- 🚧 **Advanced Builds (optional)** – Take on a challenge! These builds require you to create something with minimal guidance outside of the documentation. Completing an Advanced Build earns full credit in place of doing the base assignment notebook questions/activities.

### Main Assignment

In the following assignment, you are required to take the app that you created for the AIE9 challenge (from [this repository](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)) and conduct what is known, colloquially, as a "vibe check" on the application.

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!

> NOTE: This will require you to make updates to your personal class repository, instructions on that process can be found [here](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)!


#### A Note on Vibe Checking

>"Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.
>
>In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

---

#### 🏗️ Activity #1: General Vibe Checking Evals

Please evaluate your system on the following questions:

1. Explain the concept of object-oriented programming in simple terms to a complete beginner.
    - Aspect Tested: explanation of a relatively difficult concept. simplifying difficult concept for beginners
2. Read the following paragraph and provide a concise summary of the key points…
    - Aspect Tested: summarizing information. removing fluff from large amounts of information, and presenting a shortened, but still useful account of the text.
3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested: imaginative and creative writing. text generation. 
4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested: mathematical calculations and reasoning
5. Rewrite the following paragraph in a professional, formal tone…
    - Aspect Tested: tone modification and text/word transformation

#### ❓Question #1:

Do the answers appear to be correct and useful?
##### ✅ Answer:
the AI did not seem to retain context from previous prompts. i pasted a long paragraph to summarize, and then i instructed it to simply 'provide a shortened and concise account of that text', and it requested the text to be pasted into the context window. i then asked if it retained context, and it claimed it does. i tested this again by pasting in a paragraph to summarize, awaited a response, then instructed it to summarize the previously sent paragraph. it stated it needed me to provide the text to summarize. 

it also provided much filler text in its responses. 

during the mathematical testing prompt, i received a few strings of text like this in the response:
 \[ \text{Number of apple packs} = \frac{12 \text{ apples}}{4 \text{ apples/pack}} = 3 \text{ packs} \] 
 that is not useful to the average user, nor would they understand it. 

---

#### 🏗️ Activity #2: Personal Vibe Checking Evals (Your Assistant Can Answer)

Now test your assistant with personal questions it should be able to help with. Try prompts like:

- "Help me think through the pros and cons of [enter decision you're working on making]."
- "What are the pros and cons of [job A] versus [job B] as the next step in my career?"
- "Draft a polite follow-up [email, text message, chat message] to a [enter person details] who hasn't responded."
- "Help me plan a birthday surprise for [person]."
- "What can I cook with [enter ingredients] in fridge."

##### Your Prompts and Results:
1. Prompt: Help me think through the pros and cons of deciding whether to move to a new city for a higher-paying job that would require longer work hours and leaving behind close friends and family.
   - Result: Absolutely, it's important to weigh the pros and cons carefully. Let's break this down: ### Pros of Moving for a Higher-Paying Job: 1. **Financial Benefits**: A higher salary can lead to improved financial stability, allowing you to save more, invest, or enjoy a higher quality of life. 2. **Career Growth**: This job may offer better career prospects, professional development opportunities, and the chance to build a stronger resume. 3. **New Experiences**: Moving to a new city can be exciting and provide opportunities to meet new people, experience different cultures, and explore diverse environments. 4. **Independence**: Starting fresh in a new city can help you grow personally and become more self-reliant. 5. **Potential for Work-Life Balance Changes**: Although the job requires longer hours, there may be potential for a more flexible schedule or excellent benefits that could improve your overall life balance. ### Cons of Moving for a Higher-Paying Job: 1. **Distance from Family and Friends**: Leaving behind your support system can lead to feelings of loneliness and isolation, especially if you’re accustomed to a close-knit circle. 2. **Lifestyle Changes**: Adjusting to a new city can be challenging, from the cost of living to transportation and adapting to new social norms. 3. **Longer Work Hours**: While the pay may increase, longer hours can lead to burnout or impact your work-life balance negatively. 4. **Adjustment Period**: It may take time to find new friends and build a community, which can be stressful and daunting. 5. **Pressure of a New Environment**: The responsibility of performing well in a new job can add stress. ### Reflection Questions: - **What are your long-term career goals?** Does this job align with them? - **How much do you value your current relationships?** Can these relationships be maintained despite the distance? - **What aspects of your current lifestyle do you cherish?** Are they replaceable, or would losing them be a significant sacrifice? - **Are you prepared for the transitional phase?** Think about how you might handle feelings of isolation and stress. ### Conclusion: When making your decision, it may be helpful to prioritize what's most important to you right now. You could also create a list of your values and see how each option aligns with them. Additionally, consider discussing this with trusted friends or family to gain different perspectives. Ultimately, choose the path that feels right for you and your future aspirations.
2. Prompt: What are the pros and cons of choosing a full-time software engineer role at a large, well-established corporation versus joining a small startup as an early employee for the next step in my career?
   - Result: Choosing between a full-time software engineer role at a large, established corporation and joining a small startup as an early employee is a significant decision that can shape your career trajectory and personal satisfaction. Here are some pros and cons of each option to help you weigh your decision: ### Large Corporation **Pros:** 1. **Stability and Security:** Well-established companies usually offer job security, benefits, and a stable work environment, which can be reassuring. 2. **Structured Career Path:** Big corporations often have clear career advancement paths and professional development programs. 3. **Resources and Training:** Larger companies may provide access to extensive resources, training, and mentorship programs, allowing you to enhance your skills. 4. **Work-Life Balance:** Many larger companies prioritize work-life balance, offering flexible hours or remote work options. 5. **Network Opportunities:** You’re likely to connect with a diverse array of professionals, which can enhance your network and future opportunities. **Cons:** 1. **Less Impact:** Your role may feel less impactful in a large organization, where your contributions can be diluted in bigger teams or projects. 2. **Bureaucracy:** Larger companies often have more red tape and slower decision-making processes, which can be frustrating. 3. **Specialization:** You might find yourself pigeonholed into a specific role, limiting your ability to explore different aspects of technology or the business. 4. **Cultural Fit:** Is it a good cultural fit for you? Sometimes, the corporate culture can feel impersonal or rigid. ### Small Startup **Pros:** 1. **Impact and Ownership:** In a startup, your contributions are often more visible and can have a significant impact on the company's success. 2. **Diverse Experience:** You may wear multiple hats, gaining experience in various areas of the business and rapidly expanding your skill set. 3. **Innovative Environment:** Startups tend to foster creativity and innovation, allowing you to work on cutting-edge projects and technologies. 4. **Agility:** The decision-making process is usually faster in a startup, which can lead to more dynamic and exciting work. 5. **Cultural Fit and Values:** Startups often have a close-knit culture, where teamwork and shared values are emphasized. **Cons:** 1. **Uncertainty and Risk:** Startups come with inherent risks, including job instability and the potential for business failure. 2. **Work-Life Imbalance:** The fast-paced environment can lead to longer hours and may blur the boundaries between work and personal life. 3. **Limited Resources:** Startups often lack the resources and benefits that established companies provide, potentially leading to fewer training opportunities and benefits. 4. **Limited Career Structure:** There may be less clarity in terms of career paths and advancement opportunities, relying more on personal initiative and adaptation to growth. ### Conclusion Ultimately, your choice should reflect your personal career goals, risk tolerance, and preferences for work environments. Consider what you value most in your career at this stage—whether it's stability and resources or the chance to innovate and make a difference. It's also helpful to think about your long-term goals and where you see yourself in the future. Making a well-informed choice that aligns with your values will set you on the right path for professional fulfillment.
3. Prompt: Draft a polite and professional follow-up email to a hiring manager after a job interview when they said I would hear back within a week, but it has now been two weeks with no response.
   - Result: Subject: Follow-Up on Interview Status Dear [Hiring Manager's Name], I hope this message finds you well. I wanted to follow up regarding my interview for the [Job Title] position on [Interview Date]. I truly enjoyed our conversation and am very enthusiastic about the opportunity to join [Company Name] and contribute to your team. I understand that you mentioned I would hear back within a week, and I appreciate that these decisions can take time. If there are any updates on my application status or the next steps in the process, I would greatly appreciate it if you could share them with me. Thank you once again for the opportunity to interview for the position. I look forward to hearing from you. Best regards, [Your Name] [Your Phone Number] [Your LinkedIn Profile or any other relevant contact information] 
4. Prompt: Help me plan a thoughtful birthday surprise for my partner who enjoys cycling, good coffee, and low-key experiences rather than large parties. My budget is around $150.
    - Result: That sounds like a wonderful way to celebrate your partner’s birthday! Here’s a thoughtful plan that incorporates their love for cycling and coffee while keeping it intimate and special: ### Birthday Surprise Plan **1. Morning Bike Ride:** - **Location:** Find a scenic bike path or trail that you both enjoy or one that you've wanted to explore. - **Duration:** Plan for a leisurely ride, maybe around 1-2 hours, allowing for plenty of conversation and enjoyment of the scenery. - **Preparation:** Pack a small picnic to take with you. A simple backpack with refreshments (suggestions below) will keep things light and fun. **2. Coffee & Picnic:** - **Coffee Stop:** Before or after your ride, stop by a local coffee shop that you know they love (or try a new one with great reviews). - **Picnic:** Prepare a small picnic with some of their favorite treats: - **Food Ideas:** You could include pastries, fresh fruits, nut mixes, or sandwiches. - **Budget:** Aim to keep the total for this picnic around $30-$40. - **Setting:** Find a cozy spot along the bike path or at a park where you can relax and enjoy the food and coffee together. **3. Thoughtful Gift:** - **Gift Options:** Choose something meaningful that aligns with their interests. Here are a few ideas that can fit within your budget: - **Cycling Accessories:** A stylish water bottle, bike lights, or a new cycling jersey. - **Coffee Experience at Home:** A high-quality bag of coffee beans from a local roaster and a cute coffee accessory (like a manual coffee grinder or a pour-over set). - **Gift Voucher:** A gift card to their favorite local bike shop or a coffee shop can be a great option. - **Personal Touch:** Write a heartfelt note or poem to accompany the gift expressing your appreciation and love. **4. Evening Wind Down:** - **Relaxing Evening:** After the bike ride, you could set up a low-key evening at home. This could include: - **Cooking Together:** Prepare a simple dinner together, perhaps something they really enjoy. - **Movie Night:** Create a cozy atmosphere, pick a movie or show you both love, and enjoy it with some homemade popcorn or dessert. ### Budget Breakdown: - **Picnic & Coffee:** $30-$40 - **Gift:** $40-$80 (depending on what you choose) - **Dinner & Snacks:** $30-$50 This plan allows for a mix of outdoor adventure, quality time, and personal touches that make for a memorable day. Most importantly, it caters to their love for cycling and coffee while avoiding the hustle and bustle of a large gathering. Enjoy the celebration!
5. Prompt: What meals can I cook using chicken breast, rice, eggs, spinach, garlic, onions, soy sauce, olive oil, and basic spices that I already have at home?
    - Result: You have a great selection of ingredients! Here are a few meal ideas you can prepare using chicken breast, rice, eggs, spinach, garlic, onions, soy sauce, olive oil, and basic spices: ### 1. **Chicken and Spinach Stir-Fry** **Ingredients:** Chicken breast, spinach, garlic, onion, soy sauce, olive oil, and your choice of spices (like salt, pepper, and paprika). **Instructions:** - Slice the chicken breast into thin strips. - Heat olive oil in a pan over medium heat. - Add minced garlic and chopped onion, sauté until fragrant. - Add the chicken and cook until browned and cooked through. - Add spinach and a splash of soy sauce, cooking until the spinach wilts. - Season with your spices and serve over cooked rice. ### 2. **Egg Fried Rice with Chicken and Spinach** **Ingredients:** Cooked rice, chicken breast, eggs, spinach, garlic, onion, soy sauce, olive oil, and spices. **Instructions:** - Dice chicken breast and cook in olive oil in a pan until browned. - Remove chicken and set aside. In the same pan, add minced garlic and chopped onion, sauté until translucent. - Push them to the side of the pan and scramble the eggs in the space until cooked. - Add the cooked rice, chicken, and spinach to the pan. Pour in soy sauce and mix everything together. - Cook until heated through, season to taste, and serve hot. ### 3. **One-Pot Garlic Chicken and Rice** **Ingredients:** Chicken breast, rice, spinach, garlic, onion, olive oil, chicken broth (or water), soy sauce, and spices. **Instructions:** - In a pot, heat olive oil and sauté diced onion and minced garlic until aromatic. - Add diced chicken and cook until browned. - Stir in rice and add chicken broth (or water), soy sauce, and the spices. Bring to a boil. - Once boiling, cover and reduce heat to low, simmering until rice is cooked. - Stir in fresh spinach just before serving, letting it wilt. ### 4. **Spinach and Chicken Omelette** **Ingredients:** Eggs, chicken breast, spinach, garlic, onion, olive oil, and spices. **Instructions:** - Cook diced chicken in olive oil with minced garlic and chopped onion until the chicken is fully cooked. - Add spinach until wilted and set aside. - In a bowl, beat the eggs, season with spices, and pour them into a heated pan. - Once the eggs start to set, add the chicken and spinach mixture to one half of the omelette. Fold the other half over and cook until fully set. - Serve with rice on the side if desired. ### 5. **Chicken and Spinach Quinoa Bowl** *If you have/access to quinoa, you can substitute it for rice.* **Ingredients:** Chicken breast, spinach, garlic, onion, quinoa (or rice), olive oil, and soy sauce. **Instructions:** - Cook quinoa/rice according to package instructions. - In a skillet, heat olive oil, sauté chopped onion and garlic, add diced chicken, and cook through. - Add spinach until wilted and toss with cooked quinoa/rice and a splash of soy sauce before serving. These meals are not only delicious but also balance protein, carbohydrates, and vegetables, keeping your meals nutritious! Enjoy your cooking!


#### ❓Question #2:

Are the vibes of this assistant's answers aligned with your vibes? Why or why not?
##### ✅ Answer: this assistant's vibes do not align with my own. the responses contain too much filler, and "fluff". it also provided uneeded and unecessary content, particularly with the mathematical prompt. i don't need the llm to tell me how brilliant or curious i am. just respond to the prompt. 
it was also providing responses in markdown format, which did not lend well to the frontend UI. 
lastly, if i pressed shift+enter, to move to a new line, it would send the text input to the llm. this needs to be fixed on the frontend. 
was also slow. 

---

#### 🏗️ Activity #3: Personal Vibe Checking Evals (Requires Additional Capabilities)

Now test your assistant with questions that would require capabilities beyond basic chat, such as access to external tools, APIs, or real-time data. Try prompts like:

- "What does my schedule look like tomorrow?"
- "What time should I leave for the airport?"

##### Your Prompts and Results:
1. Prompt: Is tomorrow a good day to go hiking?
   - Result: To determine if tomorrow is a good day for hiking, you'll want to consider a few factors like the weather forecast, trail conditions, and your personal readiness. 1. **Weather**: Check the forecast for temperature, precipitation, and wind. Ideal hiking weather is usually mild, dry, and not too windy. 2. **Trail Conditions**: Consider if the trails are open and their current condition. Recent rains or snow can affect trail accessibility and safety. 3. **Personal Readiness**: Assess your physical condition and mental readiness. Are you feeling energized and excited about the hike? If the weather looks good, the trails are in good shape, and you feel ready to go, then it sounds like a great day for a hike! Whatever you decide, make sure to pack appropriately and prepare for your adventure. Enjoy!
2. Prompt: I have a concert downtown tomorrow. What time should I leave my house to get there by 7pm?
   - Result: To determine what time you should leave your house for the concert, consider a few factors: 1. **Travel Time**: How long does it take to get to the venue? Make sure to check for any traffic conditions or delays. 2. **Parking or Transportation**: If you're driving, factor in time for parking. If you're using public transport, check the schedule. 3. **Arrival Time**: It's often a good idea to arrive at least 15-30 minutes early to find your seat and get settled. As a general rule of thumb, if it takes you 30 minutes to get there, you might want to leave by 6:00 PM. If it takes longer, adjust your departure time accordingly. Safe travels, and enjoy the concert!

#### ❓Question #3:

What are some limitations of your application?
##### ✅ Answer: it does not retain any context from prompt to prompt. the responses are not formatted properly, and the frontend UI/UX needs to be tweaked. 
it's also not focused enough. this was intended to be a 'mental coach' and provide stress reflief and mindfulness tips. ideally, it would not be able to provide recommendations for for dinner, or formalize emails. 

---

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

### 🚧 Advanced Build (OPTIONAL):

Please make adjustments to your application that you believe will improve the vibe check you completed above, then deploy the changes to your Vercel domain [(see these instructions from your Challenge project)](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/main/README.md) and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

#### 🏗️ Activity #1
##### Adjustments Made:
- _describe adjustment(s) here_

##### Results:
1. _Comment here how the change(s) impacted the vibe check of your system_
2.
3.
4.
5.


## Submitting Your Homework
### Main Assignment
Follow these steps to prepare and submit your homework:
1. Pull the latest updates from upstream into the main branch of your AIE9 repo:
    - For your initial repo setup see [Initial_Setup](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)
    - To get the latest updates from AI Makerspace into your own AIE9 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `01_Prototyping_Best_Practices_and_Vibe_Check` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Edit this `README.md` file (the one in your `AIE9/01_Prototyping_Best_Practices_and_Vibe_Check` folder)
4. Complete all three Activities:
    - **Activity #1:** Evaluate your system using the general vibe checking questions and define the "Aspect Tested" for each
    - **Activity #2:** Test your assistant with personal prompts it should be able to answer
    - **Activity #3:** Test your assistant with prompts requiring additional capabilities
5. Provide answers to all three Questions (`❓Question #1`, `❓Question #2`, `❓Question #3`)
6. Add, commit and push your modified `README.md` to your origin repository's main branch.

When submitting your homework, provide the GitHub URL to your AIE9 repo.

### The Advanced Build:
1. Follow all of the steps (Steps 1 - 6) of the Main Assignment above
2. Document what you changed and the results you saw in the `Adjustments Made:` and `Results:` sections of the Advanced Build
3. Add, commit and push your additional modifications to this `README.md` file to your origin repository.

When submitting your homework, provide the following on the form:
+ The GitHub URL to your AIE9 repo.
+ The public Vercel URL to your updated Challenge project on your AIE9 repo.
