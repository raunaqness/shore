ShorePOS Coding Assignment

# How to run

Requirements:
- docker
- docker-compose

```
git clone https://github.com/raunaqness/shore_temp.git
cd shore

# build docker images
bash build.sh

# run all services
docker-compose up
```

# Notes

### Overview of features and decisions made
- All the features are implemented in both phase1 and phase2 except the business logic for Generating User Insights
- EBay API was working when I first tested it 5 days back, but apparently isn't working at the time of writing this README (getting Internal Server Error), therefore mocked responses for user insights
- used `django-celery` as the messaging service due to ease of setup. In large scale use, might use something like `Kafka` or something else, depending on the system requirement


## Docs and URLs

System Architecture Diagram

- [https://whimsical.com/shore-7uJ54nwNCMw2yheEeGqtRG](https://whimsical.com/shore-7uJ54nwNCMw2yheEeGqtRG)

- There are 2 seperate Django Apps, based on the problem statement given in the PDF file: `phase_1` and `phase_2`
- `phase_1` should be running on `localhost:8000`
- `phase_2` should be running on `localhost:8001`
- django-admin 
    - url [localhost:8000/admin/](localhost:8000/admin/)
    - username : `raunaq`
    - password : `raunaq`

### Database
- used `sqlite3` as the Database for ease of use, and so that `db.sqlite3` file can be transported with example data
- would use `postgresql` if using this in production

### CRUD

#### Phase 1
- Swagger 
    - [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

- Product Alerts
    - View all ProductAlert definitions [http://localhost:8000/alerts/get_product_alerts](http://localhost:8000/alerts/get_product_alerts)
    - Create new ProductAlert [http://localhost:8000/alerts/create_product_alert](http://localhost:8000/alerts/create_product_alert)
    

- Product Alert Results
    - View [http://localhost:8000/alerts/get_all_product_alert_results](http://localhost:8000/alerts/get_all_product_alert_results)


#### Phase 2

- User Insights
    - View Generated Insights [http://localhost:8001/insights/](http://localhost:8001/insights/)
    

