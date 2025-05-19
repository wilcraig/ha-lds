# Church of Jesus Christ of Latter-day Saints Integration in Home Assistant

This integration will provide you with up-to-date info from the Church of Jesus Christ webpage (https://churchofjesuschrist.org/my-home). Available information includes daily verse, daily quote, and weekly Come, Follow Me information. 

### Installation:
#### HACS Install
- Go to HACS in your Home Assistant instance
- Click the three dots in the top-right corner and click 'Custom repositories'
- Under repository, enter "https://github.com/b-k-a/ha-lds.git"
- Under type, put "Integration"
- Press ADD
- Search for "Church of Jesus Christ of Latter-day Saints" in the search bar
- Click on the repository and hit the "Download" button

#### Manual Install
- Download the latest release
- Extract the folder lds to <config>/custom_components/
- Restart Home Assistant

### Tasks In-progress:
- Login to allow user-specific accessibility
- Lovelace card for enhanced viewing
- Expand to more languages

### Important attributes:
| Attribute | Path |
| --- | --- |
| Come, Follow Me data | state->loaderData->routes/my-home/dashboard->widgetData->cfm |
| Daily Verse | state->loaderData->routes/my-home/dashboard->widgetData->daily->scripture |
| Daily Quote | state->loaderData->routes/my-home/dashboard->widgetData->daily->quote |
