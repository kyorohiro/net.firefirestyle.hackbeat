https://hackbeat.firefirestyle.net/

# How to release

```
$ gcloud builds submit --tag gcr.io/firefirestyle/hackbeat
$ gcloud beta run deploy --image gcr.io/firefirestyle/hackbeat --platform managed
```
