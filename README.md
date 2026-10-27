# Florida Hospital Star Ratings vs. County Demographics

Project 1 for Computational Tools for Research (Fall 2026), by Tobianna Clarke

# Question
Do certain Florida hospitals get worse Medicare star ratings depending on who owns them
(for-profit vs. non-profit) or what kind of county they are in (% Black, % Hispanic,
% uninsured)?

## Data (both free APIs, no key needed)
- CMS (Medicare) Hospital General Information: star ratings for every hospital
- CDC Social Vulnerability Index 2022: county demographics

## How to run
pip install -r requirements.txt
python floridahospitalratings.py

Results get saved in the output folder (rated_hospitals.csv and summary.txt).

## What I found
- 168 of 221 Florida hospitals have a star rating
- 59% of for-profit hospitals got 1-2 stars vs. 13% of non-profits
- Counties with more uninsured people had lower-rated hospitals, even when
  comparing only non-profits (28% low-rated vs. 6%)
- % Black: almost no difference. % Hispanic: a small gap

## What I think it means
My biggest finding was that who owns a hospital matters a lot. More than half of for profit hospitals got 1 or 2 stars, compared to only 13% of non profits. I think that could be because for profit hospitals focus more on making money, which might mean fewer staff or less spending on patient care. I expected race/location based demograhpic to matter more, but the gap between Black individuals was basically zero and the same applied for Hispanic individuals. Insurance seemed to matter more: even among non profits, hospitals in counties with lots of uninsured people were rated lower. This shows a disparity but doesn’t necesarily prove bias, because I didn’t account for things like hospital size, funding, or city vs. rural, and county data doesn’t show who actually goes to each hospital.
## AI use
I used Claude (AI) as a guide while building this. It explained each step and
helped me debug. I typed and tested the code in chunks, wrote my own comments,
and wrote the conclusions.