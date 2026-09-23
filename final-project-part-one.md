[Home](index.md) | [Final Project Part I](final_project_StutiGarg.md)

# Final Project Part I: Condemned Is Not the Same as Gone

*Which of Pittsburgh's condemned buildings are still worth saving?*

Stuti Garg | 94870 Telling Stories with Data | Fall 2026

---

## Project summary

Pittsburgh keeps a public list of every building the city has condemned. When I downloaded it this week, it had 2,895 properties on it. After matching those parcels to Allegheny County assessment records, about 2,359 of them are still standing buildings. The rest already show up as vacant land. Most people hear "condemned" and assume the building is about to be torn down. The data doesn't really support that. Only 9 of the buildings with an inspection score are rated "imminently dangerous," while 672 are rated as structurally intact with no immediate danger. Almost all of them are old, too: about 94% of the ones with a known build year went up before 1940.

My project is a data story for City of Pittsburgh staff, mainly the Department of Permits, Licenses, and Inspections (PLI), the Department of City Planning (DCP), and the Pittsburgh Land Bank. The city already scores condemned buildings for demolition priority, but that process is mostly about safety risk. I want to add the other side of the decision: what the city loses when a building comes down, including its age, its materials, its neighborhood context, and the embodied carbon already spent building it. I don't think the answer is "save everything." It's that a condemned list with thousands of buildings on it needs triage, and some of these buildings are better candidates for reuse than demolition.

**How the topic changed.** My first idea was to build a database of adaptive reuse buildings in Pittsburgh using deep learning. Once I looked at what data actually exists, I narrowed it. The city's condemned property list is public, updated daily, and joins cleanly to county assessment data, so I can tell a real story with it without training a model. Also, the list is about 93% residential, mostly single-family houses and rowhouses, so this is less about converting big warehouses into lofts and more about whether old houses get rehabbed or torn down. The roughly 160 commercial and industrial buildings on the list could be a smaller "adaptive reuse" thread in the story.

## Story structure

**One-sentence summary:** Most of Pittsburgh's condemned buildings are century-old structures that aren't in immediate danger of collapse, and a simple reuse check could help the city figure out which ones to save before it pays to tear them down.

**User story:** As a planner at the City of Pittsburgh, I want to see which condemned buildings are structurally sound and worth reusing so that I can direct limited demolition and redevelopment money where it matters most and avoid throwing away buildings (and carbon) we already have.

**Story arc** (following the Good Charts story structure):

1. **Setup / hook.** Open with the scale: thousands of buildings sit on the city's condemned list, and "condemned" sounds final. Pose the question of which ones are actually worth saving.
2. **Setup.** Show who these buildings are. They're overwhelmingly pre-1940, mostly houses and rowhouses, and nearly half have brick or masonry exteriors.
3. **Rising tension.** Show the PLI inspection scores. Most buildings sit in the middle ("compromised, possibly dangerous"), a big group is still intact, and very few are imminently dangerous. Then map them to show they're concentrated in a handful of neighborhoods like Perry South, Hazelwood, Homewood North, and Lincoln-Lemington-Belmar. Those neighborhoods absorb the most loss when buildings come down.
4. **Turning point.** Introduce the cost of demolition that doesn't appear on a budget line: embodied carbon. Reusing a building keeps the carbon already spent on it, while demolishing and rebuilding spends it again.
5. **Resolution.** A simple triage matrix that sorts every building by structural risk and reuse value into four groups: save first, salvage through deconstruction, mothball, or demolish.
6. **Call to action.** Before a city-funded demolition moves forward, run a quick reuse check and send strong candidates to the Land Bank or a rehab program.

## Initial sketches

These are rough storyboard sketches in the order the story would unfold. A few of them use the real data so I could sanity-check the patterns, but they're not final charts. The carbon chart and the triage scatter use placeholder values.

**Sketch 1: Title / hook (Setup)**
![Sketch 1: hook](sketches/01_hook.png)

**Sketch 2: How old are they? (Setup)**
![Sketch 2: year built histogram](sketches/02_age.png)

**Sketch 3: How dangerous are they really? (Rising tension)**
![Sketch 3: PLI score bar chart](sketches/03_scores.png)

**Sketch 4: Where are they? (Rising tension)**
![Sketch 4: dot map](sketches/04_map.png)

**Sketch 5: The carbon cost of a teardown (Turning point)**
![Sketch 5: carbon comparison](sketches/05_carbon.png)

**Sketch 6: Triage matrix (Resolution)**
![Sketch 6: triage matrix](sketches/06_triage.png)

**Sketch 7: Reuse check (Call to action)**
![Sketch 7: call to action](sketches/07_cta.png)

## The data

My main source is the **Condemned and Dead-End Properties** dataset, published by the City of Pittsburgh's Department of Permits, Licenses, and Inspections through the Western Pennsylvania Regional Data Center (WPRDC). It lists every condemned property in the city with its parcel ID, address, neighborhood, council district, coordinates, the date the record was created, and the latest PLI inspection score. The city's demolition engagement page explains the scoring: 1 means structurally intact with no immediate danger, 2 means structurally compromised and possibly dangerous, 3 means compromised and dangerous, and 4 means imminently dangerous. It's updated daily, so I saved a snapshot from September 23, 2026 to keep my numbers consistent.

To learn about the buildings themselves, I joined that list to the **Allegheny County Property Assessments** dataset (also on WPRDC) using the parcel ID. This gives me year built, land use, number of stories, exterior finish, the assessor's condition rating, finished living area, and assessed value. All 2,895 condemned parcels matched. For the carbon section, I plan to multiply each building's floor area by a published per-square-foot embodied carbon benchmark for new residential construction. I haven't picked the benchmark yet (I'm looking at Carbon Leadership Forum sources), so the carbon numbers are still open. I may also bring in PLI demolition permit data to show how many condemned buildings actually get torn down each year.

A few data issues I'm keeping track of:

- Some parcels show up more than once in the condemned list, with different inspection scores (568 parcels). For now I'm keeping the highest (most severe) score for each parcel to be conservative.
- 337 standing buildings have a score of 0, which isn't defined in the city's 1 to 4 scale. Most parcels coded as vacant land also have a 0, so it might mean "no structure" or "not yet scored." I'm treating these as unknown for now and plan to ask PLI.
- 588 buildings have a build year of exactly 1900, which looks like a default placeholder value. The "before 1940" finding holds either way, but I won't lean on the exact median.
- I removed owner names from the copy I'm publishing. The owner type (individual vs. corporation) is enough for this story, and I don't want to put private individuals' names on a public site.

**Data links**

- Source: [Condemned and Dead-End Properties, WPRDC](https://data.wprdc.org/dataset/condemned-properties)
- Source: [Allegheny County Property Assessments, WPRDC](https://data.wprdc.org/dataset/property-assessments)
- Scoring explanation: [City of Pittsburgh PLI Demolition Engagement](https://engage.pittsburghpa.gov/pli-demolition-engagement)
- My snapshot of the condemned list (owner names removed): [data/pli_condemned_properties_raw_2026-09-23.csv](data/pli_condemned_properties_raw_2026-09-23.csv)
- My joined, one-row-per-parcel dataset: [data/condemned_buildings_joined.csv](data/condemned_buildings_joined.csv)

## Method and medium

I'm planning to build the final story in **Shorthand**, with the charts and map made in **Tableau Public** and embedded in the story. The scrolling format fits a story that moves from "what's on this list" to "what should we do about it," and Tableau lets planners filter the map by neighborhood or council district to find buildings in their own area. I'll clean and join the data in Python (Google Colab) and keep the notebook in this repo so the process is transparent. The final step will be a downloadable "save first" list, so the story ends with something the city could actually use.

## References

Berinato, S. (2019). *Good Charts Workbook: Tips, Tools, and Exercises for Making Better Data Visualizations.* Harvard Business Review Press.

City of Pittsburgh, Department of Permits, Licenses, and Inspections. (2026). *Condemned and Dead-End Properties* [Data set]. Western Pennsylvania Regional Data Center. Retrieved September 23, 2026, from https://data.wprdc.org/dataset/condemned-properties

Allegheny County Office of Property Assessments. (2026). *Allegheny County Property Assessments* [Data set]. Western Pennsylvania Regional Data Center. Retrieved September 23, 2026, from https://data.wprdc.org/dataset/property-assessments

City of Pittsburgh. (n.d.). *Condemned properties for demolition.* Engage Pittsburgh. Retrieved September 23, 2026, from https://engage.pittsburghpa.gov/pli-demolition-engagement

