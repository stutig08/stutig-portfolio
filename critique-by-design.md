| [home page](https://stutig08.github.io/stutig-portfolio/) | [data viz examples](dataviz-examples) | [critique by design](critique-by-design) | [final project I](final-project-part-one) | [final project II](final-project-part-two) | [final project III](final-project-part-three) |

# Critique by Design: EU book prices

A MakeoverMonday redesign of a Eurostat chart, taken through critique, sketching, peer testing and a Tableau rebuild.

## Step one: the visualization
<img width="1351" height="997" alt="image" src="https://github.com/user-attachments/assets/dfde1c1c-823a-4f37-9042-a6cb968d1826" />
![Original Eurostat chart, price development in the EU, all products and books](https://stutig08.github.io/stutig-portfolio/assets/original-eurostat-chart.png)

*Source: Eurostat, ["Pick up a book and read!"](https://ec.europa.eu/eurostat/web/products-eurostat-news/-/EDN-20200422-1), 22 April 2020. Reissued as MakeoverMonday challenge 2020/W38.*

The chart plots two monthly Harmonised Index of Consumer Prices series for the EU aggregate, books and all items, both indexed to 2015 = 100, over roughly 2009 to early 2020.

I picked it because at first glance nothing is wrong with it. The data is real, the source is cited, a line chart suits a time series, and the palette is restrained. That made it a harder and more interesting critique than an obviously bad graphic would have been, and I wanted to see whether a structured method would find anything a quick look would miss.

What actually drew me in was the gap between how much data Eurostat holds and how little appears. The file behind this chart carries 17,856 monthly observations across 36 countries, from January 2000 through August 2020. The published chart shows one aggregate series over about a decade. That ratio felt like the beginning of a story before I had read a word of the article.

## Step two: the critique

I assessed the chart with Stephen Few's Data Visualization Effectiveness Profile and submitted the Google Form. My scores:

| Criterion | Score | Reasoning |
| --- | --- | --- |
| Usefulness | 5 | Supports a real, verifiable claim, but the reader has to get that claim from the prose |
| Completeness | 4 | One aggregate series from a file of 36 countries, and it ignores the genre breakdown the article itself cites |
| Perceptibility | 4 | The claim is about the gap between the lines, and the gap is the hardest thing in the chart to read |
| Truthfulness | 6 | Accurate HICP data, but the article's window, the plotted window and the labelled axis are three different periods |
| Intuitiveness | 7 | A line chart is universally readable, though the index basis is never explained |
| Aesthetics | 5 | Clean type and restrained color, undercut by decoration filling roughly 40 percent of the frame |
| Engagement | 4 | The book illustration earns a scroll-stop, then offers no payoff |

The central problem is that the chart hides its own headline. The article states the finding plainly: book prices grew more slowly than consumer prices generally, up 9 percent against 14 percent between February 2010 and February 2020. I checked both figures against the source data and they hold, at 9.5 and 14.6 percent. But that claim is about the **gap** between two series, and the chart encodes the two **levels** instead. Over the plotted window books begin above all products, 93.4 against 90.3 in January 2009, and end below, 103.0 against 105.2 in February 2020. That five-point swing is the entire story, and in a chart where both lines wander through the same narrow band at monthly resolution it is close to invisible.

Opening the data changed the critique a second time. The EU average is not a summary of a consistent pattern, it is the midpoint of a wide spread that cancels itself out. At August 2020 the Danish books index sits at 165.6 while Denmark's all-items index is 103.1. Portugal sits at 44.3 and Hungary at 63.6. Neither of those is a data error. Each series drops in a single September, Portugal by 40 index points in September 2019 and Hungary by 23 in September 2017, and both dates match national policies making school textbooks free. The EU line is averaging away the measurable effect of education policy on what households pay for books.

Two smaller findings. Indexing both series to 2015 = 100 guarantees they meet at 2015 by construction, so a mathematical artifact reads as a finding. And the open-book illustration is not neutral: its page gutter and drop shadow run vertically through the plot area right where the two lines cross. Chartjunk behind data is tolerable; chartjunk behind the most interpretively important region of the data is not.

I also measured the two companion infographics in the same article, in pixels rather than by eye, expecting distortion. There was none. The trade bars are proportional and the production stacks come in at a height ratio of 0.731 against a true 0.729, with equal widths so there is no area inflation. The real flaw is narrower: the trade bars are drawn to a zero baseline hidden behind the illustration, so a reader cannot verify proportions that happen to be correct.

**On the method.** Few's profile was more useful than I expected, mainly because separating usefulness from truthfulness from aesthetics forced me to defend a chart I had already decided I disliked. Compared with the Good Charts approach, though, it audits the artifact rather than the communication. Berinato starts from intent, from what single idea a chart is meant to land, and that framing is what surfaced the real failure here. Reading Few's criteria alone I had this marked down as a graphic with nothing to declare. Reading the source article showed it does have something to declare and simply encodes the wrong quantity to declare it. Few's seven criteria never ask what the chart is arguing, so they cannot separate a chart with no message from a chart with a buried one, and those two failures need completely different fixes. The profile also has no dimension for accessibility, none for context of consumption, and no weighting, so a decorative chart with a trivial message and a plain chart with an important one can land at similar totals.

## Step three: Sketch a solution

<img width="1742" height="1889" alt="wireframes (1)" src="https://github.com/user-attachments/assets/9017b264-3348-491d-9230-1aad5d181d9c" />

![Wireframes A and B, used for peer testing](https://stutig08.github.io/stutig-portfolio/assets/wireframes.png)

I drew two wireframes, deliberately rough so reviewers would react to structure rather than styling, and with real data rather than placeholder shapes so they would react to the actual Portugal outlier.

**Wireframe A** stacks four panels in the order a reader should meet them. A difference line, books minus all items, which answers the article's claim in one shape. A country gap chart, two dots per row connected by a bar, sorted by the gap, with Portugal and Denmark at the extremes. A sparkline grid, one small panel per country with the EU trace ghosted behind. And the original chart rebuilt honestly, kept small at the bottom as context and as a visible before-and-after.

**Wireframe B** replaces the country panel with a single sorted bar of the gap value. It carries less information, since the two underlying levels are lost, but the encoding is one length against one baseline and nobody has to work out what a connecting bar means. I held it in reserve rather than leading with it.

## Step four: Test the solution

Four people saw the sketch with no explanation. I showed it, said "take a look at this and tell me what you see," and then waited, since the first unprompted sentence is the most useful thing you get.

Questions asked:

- What do you think this is about?
- Walk me through what the top panel is telling you.
- In the second chart, what does the line between the two dots mean?
- Portugal is at the far left. What does that tell you?
- Who do you think this was made for?
- Is there anything here you would change or drop?

Results:

| Question | Interview 1 (MISM student, Heinz) | Interview 2 (Public policy student, Heinz) | Interview 3 (Graduate student, outside Heinz) | Interview 4 (CMU student, no data background) |
|---|---|---|---|---|
| What is this? | Book-price inflation against overall inflation across EU countries | Whether books became relatively more or less expensive, then how countries differ | About book prices in Europe, but did not register the top panel as a difference | Book prices changed differently across countries; the inflation comparison took longer |
| The connecting line | Read it as movement from one value to another, not a gap | Understood after checking the legend, but felt it implied direction | Unsure what it added beyond showing distance | Assumed change over time between the grey and black dots |
| Portugal | Strongest negative outlier, books rose much less than prices generally | Books much cheaper relative to inflation, read at first as prices falling | Clearly different, but had to return to the legend to say why | Most extreme on the cheaper side, "books got much cheaper there" |
| Would change | Label the two dots directly instead of relying on a legend | Preferred Wireframe B, the zero baseline made it immediate | Add a subtitle explaining positive against negative gap; too many panels competing | Preferred Wireframe B; simplify and make the takeaway prominent |
| Where I had to explain | That the line is not change over time | The difference between prices falling and prices rising more slowly | What "books minus all items" meant | That Portugal may not mean cheaper in absolute terms |

**Synthesis.**

Two patterns ran across every session. Three of four independently read the connecting line as movement through time, even though both dots are August 2020. That is not a labelling problem I could annotate away. A line between two points implies travel, and where the horizontal axis is a price index, travel along it reads as time. The encoding was fighting itself.

The second pattern I had not predicted, and it is the most useful thing that came out of this assignment. Two reviewers read Portugal's position as meaning book prices had fallen, and I corrected them both. I was wrong to do that. Portugal's books index stands at 44.3 against a 2015 base of 100, so book prices there fell by roughly 56 percent in absolute terms. The reviewers read the chart correctly and I talked them out of it.

Checking the full set made it worse, and more interesting. Of the 17 EU geographies with a negative gap in August 2020, 9 had a genuine absolute decline in the books index and only 8 merely lagged inflation. So the gap chart silently merged two different facts into one visual position, and a reader could not tell which they were looking at. I had built the chart and still got it wrong under questioning. The original Eurostat chart buried its message; my redesign encoded one that was ambiguous between two meanings. Mine is arguably the more dangerous failure, because it looks decisive.

I had written five predictions before the interviews so I could be scored against them. Three held. One was half right: the difference line landed faster for the two Heinz reviewers but not for the outside reviewer. One was wrong in a way that mattered. I expected Portugal to be read as a data error before it was read as a finding, and instead all four accepted it as real immediately and then misread what it meant. A chart that makes a true outlier believable but its meaning wrong is a harder problem than one that makes readers suspicious.

**Design changes going into the build.**

1. The dumbbell becomes Wireframe B, one bar per country against a zero baseline. This is the change I least wanted to make, since the dumbbell was the idea I was attached to, but three of four misread it and two preferred the alternative unprompted.
2. The absolute decline gets its own encoding, so the nine countries where prices actually fell stop looking identical to the eight that merely lagged.
3. The subtitle states the index in plain words, which is the fix for the reviewer who did not recognise what the top panel measured.
4. The sparkline grid is cut. Nobody drew anything from it and two reviewers said the layout was crowded.
5. Direct labels replace the legend wherever a legend survives.

## Step five: build the solution

<iframe
  src="https://public.tableau.com/views/EUbookpricesMakeoverMonday2020W38_/EUbookprices?:showVizHome=no&:embed=true"
  width="100%" height="1600" frameborder="0" scrolling="no">
</iframe>

[Open the full dashboard on Tableau Public](https://public.tableau.com/app/profile/stuti.garg4065/viz/EUbookpricesMakeoverMonday2020W38_/EUbookprices)

The redesign answers two questions the original left on the table.

The top panel is the article's own claim turned into a picture: one difference line, books minus all items, with a zero rule through it. Books sit above the line through the 2000s, cross around 2011, and stay below through 2020. That shape is the finding Eurostat stated in prose and never encoded. It took one line where the original used two.

The lower panel is what the EU average conceals. Every EU member state plus the aggregate, sorted by the gap, split into three labelled bands: countries where book prices fell outright since 2015, countries where books rose but more slowly than inflation, and countries where books outpaced inflation. The banding is the direct fix for the ambiguity my reviewers exposed, because the band header says in words which of the two facts a bar represents. Portugal and Hungary are annotated with the textbook policies that explain them, so the two most extreme values arrive with their reason attached instead of looking like errors.

What I tried to do differently comes down to three things. Encode the quantity the claim is actually about, rather than the two levels it is derived from. Show the distribution instead of the average, because this average is a midpoint of opposites rather than a summary of a pattern. And put the explanation for the outliers on the chart, since the most interesting thing in this dataset is that national education policy shows up in a consumer price index.

**On the process.** The critique changed three times, and that is the part worth recording. It changed when the data showed the EU average was concealing a wide spread. It changed again when the source article revealed the chart had a real, verified claim it was failing to encode. And it changed a third time when peer testing revealed my own redesign had introduced an ambiguity the original did not have. Critique by design turned out to be less about diagnosing someone else's chart than about discovering that the same failure modes are easy to reproduce, and that the fastest way to find them is to hand a sketch to four people and stay quiet.

## References

- Eurostat, ["Pick up a book and read!"](https://ec.europa.eu/eurostat/web/products-eurostat-news/-/EDN-20200422-1), 22 April 2020. Original chart and article.
- Eurostat, Harmonised Index of Consumer Prices, table `prc_hicp_midx`, monthly, obtained via MakeoverMonday 2020/W38.
- Stephen Few, ["Data Visualization Effectiveness Profile"](http://www.perceptualedge.com/articles/visual_business_intelligence/data_visualization_effectiveness_profile.pdf), Perceptual Edge, 2017.
- Scott Berinato, *Good Charts*, chapters 3 and 4.
- The Portugal News, ["Free school books in state schools"](https://www.theportugalnews.com/news/free-school-books-in-state-schools/50454), on the July 2019 law.
- Hungarian government family portal, ["Ingyenes tankönyvellátás"](https://csalad.hu/tamogatasok/ingyenes-tankonyvellatas), on the 2017/18 extension to grades 5 to 9.

## AI acknowledgements

I used Claude throughout this assignment. It profiled the Eurostat dataset, verified the article's percentage claims against the source data, traced the Portugal and Hungary outliers to national free-textbook policies, prepared the cleaned Tableau input file, and drafted the wireframes and much of the writing on this page. I verified the policy dates against the sources cited above, ran the four peer interviews, made the design decisions that followed from them, and built the published Tableau dashboard.
