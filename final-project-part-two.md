| [home page](./) | [data viz examples](dataviz-examples) | [critique by design](critique-by-design) | [final project I](final-project-part-one) | [final project II](final-project-part-two) | [final project III](final-project-part-three) |

# Final Project Part II: Condemned Is Not the Same as Gone

*Which of Pittsburgh's condemned buildings are still worth saving?*

**[Draft ArcGIS StoryMap: Condemned Is Not the Same as Gone](https://arcg.is/0rSOGK1)**

## What changed since Part I

The Part I feedback gave me a few clear directions, and I built them into this draft:

- **Medium.** I switched from Shorthand to ArcGIS StoryMaps. This story is about specific buildings in specific neighborhoods, and StoryMaps lets the map carry the narrative: readers can click any condemned building, zoom through the most affected neighborhoods, and swipe between condemned buildings and demolitions. It's also the platform the City of Pittsburgh uses for its open data, which fits my audience.
- **Change over time.** I added the city's PLI demolition permit data, so the story now shows how fast buildings actually come down compared with how many are waiting on the condemned list.
- **Map context.** The map now shows Pittsburgh's neighborhood boundaries, shaded by the number of condemned buildings, so readers can see exactly which communities are affected.
- **Neighborhood conditions.** I added a census tract layer on housing complaints and housing values that I first built in a GIS course (48-569) in Spring 2026. It shows that condemned buildings sit in areas with wider housing distress.
- **Introducing concepts.** The city's 1 to 4 inspection scale is written out directly on the score chart, so readers who don't work in planning can follow it.
- **Which score to highlight.** One reviewer suggested highlighting score 2 instead of score 1. When I checked the city's definitions again, score 2 means "structurally compromised, unsafe, and possibly dangerous," so I don't think I can call those buildings harmless. I kept score 1 as the highlight and now frame score 2 as the "could go either way" group, which is exactly where triage matters most.

# Wireframes / storyboards

The story moves through eight parts, each with one main message and one main visual. The overview below shows the full sequence. The [draft StoryMap](https://arcg.is/0rSOGK1) builds these out with an interactive map, neighborhood zooms, and a swipe comparison.

![Storyboard overview](storyboard/00_storyboard_overview.png)

| # | Section | Main message | Visual |
|---|---|---|---|
| 1 | Hook | Thousands of Pittsburgh buildings are condemned, but condemned doesn't mean gone. | Big number callout |
| 2 | How dangerous are they? | Very few are about to collapse; a large group is still intact. | Bar chart of PLI scores |
| 3 | Who are these buildings? | They're mostly century-old houses. | Histogram of year built |
| 4 | Where are they? | They cluster in a handful of neighborhoods with wider housing distress. | Interactive map with neighborhood zooms, plus tract-level housing complaints |
| 5 | The math doesn't work | The city demolishes far fewer buildings each year than are waiting. | Demolition permits by year, plus a swipe map of condemned buildings vs. demolitions |
| 6 | The cost of a teardown | Demolition throws away embodied carbon that was already spent. | Text for now; carbon comparison in progress |
| 7 | A better way to decide | Not every condemned building needs the same answer. | Triage grid |
| 8 | Call to action | Run a reuse check before a city-funded demolition. | Four-step reuse check |

## Draft data visualizations

**1. Hook.** The story opens with one big number instead of a chart: 2,359 condemned buildings are still standing, but only 9 are rated imminently dangerous and 672 are rated intact.

![Hook](storyboard/01_hook.png)

**2. How dangerous are they?** Score 1 is blue and score 4 is orange; scores 2 and 3 stay grey. Buildings scored 0 (not on the city's scale) or with no score are listed in the source note.

![PLI scores](storyboard/02_scores.png)

**3. Who are these buildings?** About 94% of buildings with a known build year went up before 1940. The note flags that 588 records list exactly 1900, which looks like a placeholder year.

![Year built](storyboard/03_year_built.png)

**4. Where are they?** In the StoryMap this is an interactive map: dots colored by inspection score over neighborhoods shaded by count. Clicking a building shows its address, year built, exterior, stories, living area, inspection score, and draft triage group. The sidecar zooms into Perry South, the Homewood and Lincoln-Lemington-Belmar area, and Hazelwood, then switches to a tract layer showing housing complaints.

![Map](storyboard/04_map.png)

**5. The math doesn't work.** From 2021 to 2025, the city issued an average of 157 full demolition permits a year. At that pace, clearing today's list would take at least 15 years, even if nothing new were condemned. I kept the two numbers separate instead of putting them on two y-axes. The StoryMap follows this with a swipe map comparing condemned buildings and demolition permits.

![Demolition pace](storyboard/05_demolition_pace.png)

**6. The carbon cost of a teardown.** Still in progress until I choose a per-square-foot embodied carbon benchmark.

**7. A better way to decide.** A grid of PLI score against a draft reuse screen (built before 1940, masonry exterior). With this rule, 640 buildings land in "save first," 229 in "salvage," 1,052 in "mothball," and 26 in "demolish." The rule is a starting point, and I want to keep testing whether it makes sense to readers.

![Triage](storyboard/06_triage.png)

**8. Call to action.** A four-step reuse check the city could run before approving a city-funded demolition.

# User research

## Target audience

My main audience is City of Pittsburgh staff who make decisions about condemned buildings, especially people in the Department of Permits, Licenses, and Inspections (PLI), the Department of City Planning, and the Pittsburgh Land Bank. They know the city and the demolition process, but they may not think about building reuse or embodied carbon as part of that decision. A secondary audience is community groups and residents in the most affected neighborhoods.

It wasn't realistic to interview city staff this week, so I looked for people who are close to that audience in how they think about buildings and policy:

- people with planning, public policy, or real estate backgrounds, who read data the way a city analyst would
- people with architecture or building science backgrounds, who can judge whether the reuse argument holds up
I interviewed four CMU graduate students, one at a time: two from Heinz College (policy and data perspective) and two from the School of Architecture (buildings and design perspective). I describe them only by program. I did not interview a Pittsburgh resident outside these fields this round, which is a limitation I'd like to address in Part III.

## Interview script

**Intro (read aloud):** "I'm working on a data story about condemned buildings in Pittsburgh. I'll show you a draft and ask a few questions. There are no right answers. I'm testing the story, not you."

| Goal | Questions to Ask |
|------|------------------|
| Understand what readers assume before seeing the data | 1. Before looking at anything, what comes to mind when you hear that a building is "condemned"? |
| Check whether the main message comes through | 2. (After the opening and score chart) In your own words, what is this story about so far? |
| Find confusing labels, colors, or scales | 3. (After the score and age charts) What's the main takeaway from each chart? Is anything confusing? |
| Test whether the map is readable and useful | 4. (On the map) What stands out to you? Can you find a neighborhood you know? Did you try clicking a building? |
| Test whether the demolition pace number is trusted | 5. (After the demolition chart and swipe) Does this change how you see the condemned list? Do you trust the number? |
| Test whether the reuse and triage argument is convincing | 6. (After carbon and triage) Does the case for reusing some buildings feel convincing? Does the four-group split make sense? |
| See whether the story leads to action | 7. If you worked for the city, what would you do after reading this? What's missing? |
| Prioritize what to keep and cut | 8. What was the most memorable part? What could be cut? Was anything missing that you expected to see? |

## Interview findings

I conducted four informal user interviews with graduate students at Carnegie Mellon University: two students from Heinz College and two students from the School of Architecture. The interviews were conducted conversationally while participants reviewed the draft StoryMap.

I did not audio-record the interviews, so the findings below are reconstructed from notes and my recollection of the conversations. The responses are therefore paraphrased rather than presented as direct quotations.

One of the clearest findings was that **awareness of condemned buildings varied substantially**. Two of the four participants did not know that condemned buildings were a significant issue in Pittsburgh before seeing the StoryMap. This showed me that my story needs to provide more context at the beginning rather than assuming that readers already understand what condemnation means or how widespread the issue is.

The other two participants were more familiar with the general issue, but they became more curious once they could see the buildings spatially and understand how the problem is distributed across Pittsburgh neighborhoods.

All four participants generally found the topic interesting, but a recurring critique was that the **graphics and visual presentation could be stronger**. The maps were useful, but some of the supporting graphics could be simplified, labeled more clearly, or redesigned so that the main takeaway is immediately apparent.

Participants also responded positively to being able to move from a citywide view to specific neighborhoods and buildings. This reinforced my decision to use ArcGIS StoryMaps rather than a primarily text-based storytelling platform.

| Question / Area | Interview 1, Heinz graduate student | Interview 2, Heinz graduate student | Interview 3, Architecture graduate student | Interview 4, Architecture graduate student |
|---|---|---|---|---|
| Prior awareness of condemned buildings | Was not very familiar with condemned buildings as a Pittsburgh issue and needed some explanation of what the designation meant. | Had some awareness of vacant and deteriorated buildings but had not thought specifically about the condemned-building dataset. | Was more familiar with the idea through architecture and the built environment, but was interested in seeing the scale of the issue mapped. | Had limited prior knowledge of the issue and was surprised by how many individual properties appeared in the dataset. |
| Initial reaction | The topic became more interesting after seeing that the issue was concentrated differently across neighborhoods. | Was curious about what happens to a property after it becomes condemned and whether demolition is always the next step. | Was interested in the actual buildings and how their physical condition relates to neighborhood-level patterns. | Became curious about whether some buildings could be reused rather than demolished. |
| Maps | Found the map useful for understanding the scale of the issue but suggested making the main takeaway clearer before asking the reader to explore. | Liked being able to click and explore individual locations but felt that the legend and explanation could be more prominent. | Thought the spatial component was one of the strongest parts because the problem is inherently connected to buildings and neighborhoods. | Found the transition between the citywide and building scale useful but felt the visual hierarchy could be stronger. |
| Graphics | Felt that some graphics needed clearer labels and stronger emphasis on the main number or takeaway. | Suggested simplifying some visual information rather than showing too many elements at once. | Wanted the visualizations to feel more consistent with the map and overall StoryMap design. | Thought some graphics could communicate the story faster with less explanatory text. |
| Story / narrative | Needed more introductory context before the data-heavy sections. | Wanted a clearer explanation of why the problem persists and what happens after condemnation. | Was interested in the transition from condemnation to demolition or possible reuse. | Wanted the story to connect individual buildings more explicitly to the larger citywide issue. |
| Most useful insight for revision | Explain condemnation earlier and assume less prior knowledge. | Clarify the process and make key numbers easier to identify. | Keep individual buildings and neighborhood context central to the story. | Improve graphics and strengthen the reuse/demolition part of the narrative. |

### Overall synthesis

The interviews revealed three major areas for improvement.

First, I need to **better introduce the issue**. Because two participants had little or no prior awareness of condemned buildings as a Pittsburgh issue, the opening should briefly explain what a condemned building is and why it matters.

Second, the interviews showed that **the visual hierarchy needs improvement**. The maps were generally useful, but supporting graphics should communicate their main takeaway more immediately through stronger labels, annotations, titles, and simplified visual design.

Third, participants were particularly curious about **what happens after a building is condemned**. Questions about demolition, how long buildings remain on the condemned list, and whether some structures could instead be reused suggest that this should become a stronger narrative thread in the final version.

# Identified changes for Part III

| Research synthesis | Anticipated changes for Part III |
|---|---|
| Two participants had little prior knowledge of condemned buildings as a Pittsburgh issue. | Add an introductory section explaining what condemnation means, why properties become condemned, and why the issue matters. |
| Participants wanted to understand what happens after condemnation. | Strengthen the section explaining the relationship between condemnation, demolition, prolonged vacancy, and potential reuse. |
| Participants found the maps useful but some visual information required more interpretation. | Improve legends, annotations, map titles, and transitions between citywide, neighborhood, and individual-building scales. |
| Graphics were consistently identified as an area for improvement. | Redesign the most important graphics with clearer hierarchy, fewer competing elements, and more prominent headline takeaways. |
| Participants were curious about specific buildings rather than only aggregate statistics. | Continue using individual properties and neighborhood examples to make the larger dataset more tangible. |
| Some readers may have policy knowledge while others approach the topic through architecture or design. | Keep the language accessible while retaining enough quantitative and spatial detail for more informed readers. |
| My own review: the carbon section has no numbers yet. | Choose a published embodied carbon benchmark and add a reuse vs. demolish-and-rebuild comparison. |
| My own review: the triage screen only uses age and material. | Test adding a location factor, such as distance to transit, using transit stop data from my GIS coursework. |

### Final thoughts

The interviews were particularly useful because the participants came from two different academic contexts. Even within this relatively informed graduate-student audience, prior knowledge of condemned buildings varied substantially.

The strongest lesson for Part III is that the story should not simply present the dataset. It needs to help the reader understand **what condemnation means, where the buildings are, why they remain there, and what could happen to them next**.

The geographic storytelling approach appears to be working, so I plan to keep the maps central while improving the supporting graphics and explanatory narrative.

## References

City of Pittsburgh, Department of Permits, Licenses, and Inspections. (2026). *Condemned and Dead-End Properties* [Data set]. Western Pennsylvania Regional Data Center. Retrieved September 23, 2026, from https://data.wprdc.org/dataset/condemned-properties

City of Pittsburgh, Department of Permits, Licenses, and Inspections. (2026). *PLI Permits* [Data set]. Western Pennsylvania Regional Data Center. Retrieved September 28, 2026, from https://data.wprdc.org/dataset/pli-permits

City of Pittsburgh. (2026). *Neighborhoods* [Data set]. Western Pennsylvania Regional Data Center. Retrieved September 28, 2026, from https://data.wprdc.org/dataset/neighborhoods2

Allegheny County Office of Property Assessments. (2026). *Allegheny County Property Assessments* [Data set]. Western Pennsylvania Regional Data Center. Retrieved September 23, 2026, from https://data.wprdc.org/dataset/property-assessments

City of Pittsburgh. (n.d.). *Condemned property demolition.* EngagePGH. Retrieved September 23, 2026, from https://engage.pittsburghpa.gov/pli-property-demolition

Census tract housing complaints and housing values layer: prepared in 48-569 Geospatial Data Analytics in Infrastructure Planning, Carnegie Mellon University, Spring 2026. 

Data files: [data folder](https://github.com/stutig08/stutig-portfolio/tree/main/data)

## AI acknowledgements

I used Claude (Anthropic) as an assistant on this part of the project. It prepared the data files and gave me guidance for building the web map and StoryMap, and I built the web map and StoryMap in ArcGIS myself, published the census tract layer from my own GIS coursework, conducted all of the interviews, and wrote the findings and planned changes based on what my interviewees told me.
