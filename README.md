# Job-Finder-Beautifulsoup
This program scrapes a job board website and finds python developer jobs. The program is made using Python and the beautiful soup library.
Main features of the program are: 
  Jobs can be selected based on the required skills matching your skills.
  Selects only new jobs done by only using jobs with the "posted few days ago" tag.
  Goes through the jobs initially to filter out the undesired ones that include the skills you don't have.
  Goes through the jobs a second time and only uses the jobs that don't match with the list of undesired jobs.
  Writes each job along with the company name, required skills and a link that provides more info in a seperate file in a folder.
