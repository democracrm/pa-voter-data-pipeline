# pa-voter-data-pipeline
Data processing pipeline for PA SURE statewide voter registration data. The current focus is on preparing the data for
ingestion for other systems (such as SQL databases); further work to enrich the data is being considered once the initial
work is complete.

**NOTE**: You will have to [acquire the actual data yourself](https://www.pavoterservices.pa.gov/pages/PurchasePAFULLVoterExport.aspx);
state law prohibits its distribution (4 Pa. Code sections 183.13 (g) & 183.14 (k)).

Full Voters Export List
Full export of all voters in the county containing the following fields:
- Voter ID number
- name
- sex
- date of birth
- date registered
- status (i.e., active or inactive)
- date status
- last changed
- party residential address
- mailing address
- polling place
- date last voted
- all districts in which the voter votes (i.e., congressional, legislative, school district, etc.)
- voter history 
- date the voter’s record was last changed.
