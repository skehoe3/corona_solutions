# corona_solutions
The project was created as part of the Data Natives #hackcorona event, March 22, 2020.

The goal of this repository is to help people who find themselves with lots of time currently, for example because they have been sent home as demand for their company's products has collapsed but want to do something useful with their time and try to help people and companies in need due to the current coronavirus situation by providing their skills. 

To that end, we created a Google Form for companies or private people who need help, and another one for people want to provide their workforce.  The form data is saved to a Google sheet, which our system then requests data from via an API call. Finally, we match those people who want to do something to those requesting help based on time availability and the skills needed.

Currently, this is a basic approach to matching where for each helping hand, we simply look for all offers that match the criteria (regarding location, skillset and time).

The goal however is to have a matchmaking algorithm across all the data, so the number of overall matching pairs is maximized. For example: If you provide skill X, Y and Z and you are the only one offering skill X at a given time, the algorithm should assign you to the task which requires skill X ... even though you could also be useful for a task which requires skill Y.
