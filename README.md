# Church of Jesus Christ of Latter-day Saints Integration in Home Assistant

This integration will provide you with up-to-date info from the Church of Jesus Christ webpage (https://churchofjesuschrist.org/my-home). Available information includes daily verse, daily quote, and weekly Come, Follow Me information. 

### In-progress:
- Login to allow user-specific accessibility
- Lovelace card for enhanced viewership

### Important attributes:
| Attribute | Path |
| --- | --- |
| Come, Follow Me data | state->loaderData->routes/my-home/dashboard->widgetData->cfm |
| Daily Verse | state->loaderData->routes/my-home/dashboard->widgetData->daily->scripture |
| Daily Quote | state->loaderData->routes/my-home/dashboard->widgetData->daily->quote |
