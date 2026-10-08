| [home page](./) | [data viz examples](dataviz-examples) | [critique by design](critique-by-design) | [final project I](final-project-part-one) | [final project II](final-project-part-two) | [final project III](final-project-part-three) |

# The final data story

## [Condemned Is Not the Same as Gone](https://storymaps.arcgis.com/stories/a37cfeb23ca5488ca5d522191bb1135f)

*Which of Pittsburgh's condemned buildings are still worth saving?* An ArcGIS StoryMap by Stuti Garg, October 2026.

Pittsburgh has 2,359 condemned buildings still standing. Only 9 are rated imminently dangerous, and 672 are rated structurally intact. The story follows these buildings from what "condemned" means, to who they are, where they cluster, who lives around them, and why the city can't demolish its way through the list. It ends with a simple triage and a reuse check the city could run before approving a demolition.

- Final story: [https://storymaps.arcgis.com/stories/a37cfeb23ca5488ca5d522191bb1135f](https://storymaps.arcgis.com/stories/a37cfeb23ca5488ca5d522191bb1135f)
- Portfolio and data: [GitHub repository](https://github.com/stutig08/stutig-portfolio) · [data folder](https://github.com/stutig08/stutig-portfolio/tree/main/data)
- Earlier stages: [Part I: pitch, sketches, and data](final-project-part-one) · [Part II: storyboard and user research](final-project-part-two)

# Changes made since Part II

Part II ended with a working draft StoryMap and a list of changes based on four user interviews and feedback from the teaching team. Most of my time in Part III went into three things: making the story readable for someone who has never thought about condemned buildings, adding the context reviewers asked for, and making the whole thing look like one finished piece instead of a set of drafts.

**Restructuring the story.** In Part II the sections were long questions, which didn't fit in the StoryMap navigation bar. I reorganized the story into eight short sections (Introduction, Buildings, Map, Who's Affected, Backlog, Carbon Cost, Triage, Next Steps), each with a short heading for navigation and a full-sentence subheading underneath. This made the story easier to scan and gave it a clear arc: what the problem is, where it is, who carries it, why it persists, what it costs, and what to do.

**Adding the context reviewers and interviewees asked for.** Two interviewees didn't know condemned buildings were an issue in Pittsburgh, so the story now opens with a short, plain-language definition of what condemnation means and what happens after. Feedback on Part II pointed out that the most affected neighborhoods are predominantly Black and lower-income, so I added a new section, Who's Affected. It uses American Community Survey data by census tract. The 30 tracts with the most condemned buildings hold three out of four of the city's standing condemned buildings, are about 49% Black compared with 22% citywide, and have a typical median household income of about $42,000 compared with $72,000 elsewhere. Part I feedback asked for historical context, so I added a short paragraph on Pittsburgh's population peaking in 1950 and falling by more than half. Part I feedback also asked about change over time, which the Backlog section answers with demolition permits by year and a swipe map.

**Finishing the carbon and triage sections.** In Part II the carbon section was a placeholder. I used the Carbon Leadership Forum's 2017 benchmark study, which reports that new low-rise residential construction typically emits less than 500 kg CO2e per square meter for structure, foundation, and enclosure. Applied to the 1.06 million square feet of living area in the 640 "save first" buildings, rebuilding that space could release up to about 49,000 tonnes of CO2e. I framed this as an upper-end estimate, since the benchmark is an upper typical value. I also added a location factor to the triage using current Pittsburgh Regional Transit stop data, building on transit work from an earlier GIS course: 329 of the 640 "save first" buildings are within 400 meters of a stop with frequent service.

**Bringing in earlier GIS work.** This project grew out of an assignment in Geospatial Data Analytics in Infrastructure Planning (48-569) in Spring 2026, where I first geocoded Pittsburgh's condemned buildings and compared them with housing complaints by census tract. That tract layer appears on the fifth map slide. Two other ideas from that course shaped the final story: vacancy patterns (now covered with current ACS vacancy data) and the method of combining several risk factors to prioritize buildings, which became the triage.

## The audience

My primary audience is City of Pittsburgh staff who make decisions about condemned buildings, especially in the Department of Permits, Licenses, and Inspections, the Department of City Planning, and the Pittsburgh Land Bank. They know the demolition process well, but they may not weigh building reuse, embodied carbon, or neighborhood equity when they decide what to tear down. My secondary audience is residents and community groups in the most affected neighborhoods.

The interviews pulled the story in two directions. My interviewees were graduate students in policy and architecture, and two of them didn't know condemnation was a significant issue at all. A reviewer pointed out that city staff would already understand the basics. I handled this by keeping the explainer to one short paragraph that experts can skim and newcomers need, and by letting the charts and map carry most of the argument instead of adding long text.

Specific adjustments for this audience:

- **Use the city's own terms.** The story uses the city's 1 to 4 inspection scale and labels exactly as PLI defines them, so staff can map the story directly onto their own records.
- **End with a concrete action, not a general plea.** The Next Steps section is a four-question reuse check that could fit into an existing demolition review, plus a downloadable list of the 640 "save first" buildings, sorted with transit-accessible buildings first.
- **Be careful with claims.** Captions note where a chart shows a pattern rather than a cause, where a number is an upper-end estimate, and where the triage is a draft rule rather than a city standard. For a policy audience, overclaiming would cost credibility.

## Final design decisions

**Platform.** I switched from Shorthand to ArcGIS StoryMaps in Part II because this story is about specific buildings in specific places. StoryMaps let me build a sidecar that zooms from the whole city into Perry South, the Homewood area, and Hazelwood, plus a swipe map comparing condemned buildings with demolitions. It's also the platform the City of Pittsburgh uses for its open data.

**Interactive maps.** Every condemned building is a point on the map. Clicking one shows its address, neighborhood, inspection score, year built, exterior material, stories, living area, and draft triage group. I renamed every layer and field (for example, "PLI_Score_Label" became "Inspection score") so nothing in the legend or pop-ups reads like raw data.

**Native charts instead of images.** In Part II my charts were static images made in Python. For the final version I rebuilt the three main charts (inspection scores, year built, demolitions per year) as native StoryMaps charts, so they're interactive, resize on phones, match the story's fonts, and carry a data source note. I used exact counts in every chart and turned on data labels, which mattered for the inspection chart, where the 9 imminently dangerous buildings make a bar too thin to read without a label.

**One color system.** Blue means intact or "save first," orange means imminently dangerous or "demolish," grey is everything in between, and purple shades neighborhoods by count. The same colors run through the map, the charts, the scatter plot, and the triage grid. I rebuilt the scatter plot and triage grid in the story's dark theme so they don't look pasted in.

**What I chose not to do.** I left out a separate chart of housing complaints. The relationship is already shown on the map, and adding a second scatter plot would have pulled the story into the weeds, which Part II feedback warned about. I also merged the 1960s to 1980s into one bar in the year built chart, because those decades held only 37 buildings and the chart has a row limit.

**What I learned.** The biggest lesson was how much the data changed the story. My original pitch was about adaptive reuse with deep learning. Once I looked at the city's actual condemned list, the story became about century-old houses, inspection scores, and who lives near them, which is a smaller and more honest story with a clearer ask. I also learned how much credibility depends on small things: exact numbers instead of rounded ones, consistent terms, and captions that say what a chart does not show.

## References

All sources are also listed in the Credits section at the end of the StoryMap.

**Data**

- City of Pittsburgh, Department of Permits, Licenses, and Inspections. (2026). *Condemned and Dead-End Properties* [Data set]. Western Pennsylvania Regional Data Center. Retrieved September 23, 2026, from https://data.wprdc.org/dataset/condemned-properties
- City of Pittsburgh, Department of Permits, Licenses, and Inspections. (2026). *PLI Permits* [Data set]. Western Pennsylvania Regional Data Center. Retrieved September 28, 2026, from https://data.wprdc.org/dataset/pli-permits
- Allegheny County Office of Property Assessments. (2026). *Allegheny County Property Assessments* [Data set]. Western Pennsylvania Regional Data Center. Retrieved September 23, 2026, from https://data.wprdc.org/dataset/property-assessments
- City of Pittsburgh. (2026). *Neighborhoods* [Data set]. Western Pennsylvania Regional Data Center. Retrieved September 28, 2026, from https://data.wprdc.org/dataset/neighborhoods2
- Pittsburgh Regional Transit. (2026). *PRT Stops* [Data set]. Western Pennsylvania Regional Data Center. Retrieved October 7, 2026, from https://data.wprdc.org/dataset/prt-of-allegheny-county-transit-stops
- U.S. Census Bureau. (2025). *American Community Survey 5-year estimates, 2020 to 2024* (Tables B03002, B19049, B25002), accessed via Esri Living Atlas, "ACS Race and Hispanic Origin" and "ACS Population and Housing Basics." Retrieved October 7, 2026.
- Allegheny County. (2020). *Allegheny County Census Tracts 2020* [Data set]. Western Pennsylvania Regional Data Center. Retrieved October 7, 2026, from https://data.wprdc.org/dataset/allegheny-county-census-tracts-2020
- Census tract housing complaints and housing values layer. Data provided in course materials for 48-569 Geospatial Data Analytics in Infrastructure Planning (Prof. Kristen Kurland), Carnegie Mellon University, Spring 2026; spatial join and analysis by Stuti Garg.
- U.S. Census Bureau. (1950, 2020). *Decennial Census of Population*: City of Pittsburgh, 676,806 (1950) and 302,971 (2020). Figures as compiled in "Pittsburgh," Wikipedia, historical population table. Retrieved October 7, 2026, from https://en.wikipedia.org/wiki/Pittsburgh

**Research and definitions**

- Simonen, K., Rodriguez, B., Barrera, S., Huang, M., McDade, E., & Strain, L. (2017). *Embodied Carbon Benchmark Study: LCA for Low Carbon Construction, Part One.* Carbon Leadership Forum, University of Washington. Retrieved October 7, 2026, from https://digital.lib.washington.edu/bitstreams/e51b48fc-60db-4f42-9df9-da0f8ddf9348/download
- National Trust for Historic Preservation, Preservation Green Lab. (2011). *The Greenest Building: Quantifying the Environmental Value of Building Reuse.* Retrieved October 7, 2026, from https://www.bostonpreservation.org/resource-item/greenest-building-quantifying-environmental-value-building-reuse
- City of Pittsburgh. (n.d.). *Condemned property demolition.* EngagePGH. Retrieved September 23, 2026, from https://engage.pittsburghpa.gov/pli-property-demolition
- Wolfson, C. (2026, January 29). *Maps: Pittsburgh has more decaying homes than it can demolish.* Pittsburgh's Public Source. https://www.publicsource.org/pittsburgh-maps-demolitions-condemned-properties/

**Images and software**

- Cover image: Map by Stuti Garg; data: City of Pittsburgh PLI, Condemned and Dead-End Properties, via WPRDC (September 2026).
- All charts, maps, and diagrams were created by me from the data sources above.
- Maps and story built with Esri ArcGIS Online and ArcGIS StoryMaps (Carnegie Mellon University license), using the Esri Light Gray Canvas basemap. Scatter plot and triage grid made in Python (matplotlib).

**My data files:** [data folder on GitHub](https://github.com/stutig08/stutig-portfolio/tree/main/data), including the downloadable [draft "save first" list](https://stutig08.github.io/stutig-portfolio/data/save_first_buildings_draft.csv).

## AI acknowledgements

I used Claude (Anthropic) in this project. In Part III, it downloaded and processed the American Community Survey and transit stop data, joined them to the condemned buildings data and gave some guidance for the StoryMap in ArcGIS. 

# Final thoughts

The part of this project I'm proudest of is the shift from "here is a dataset" to "here is a decision the city makes every week, and here's a better way to make it." The most surprising finding for me was how concentrated the problem is: three out of four standing condemned buildings sit in about a quarter of the city's census tracts.

If I had more time, I would interview city staff directly, since my interviews were with graduate students rather than my actual audience. I would also refine the reuse screen with better building-condition data, test the 400-meter transit threshold against other walking distances, and look at what has happened to buildings that came off the condemned list without being demolished, which would show whether reuse is already happening.
