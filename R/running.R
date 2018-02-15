library(tidyverse)
library(lubridate)

fetchData<-read_csv(file.choose())

fetchData$Date<-dmy(fetchData$Date)

fetchData$Miles <- ifelse(fetchData$Unit == "km",fetchData$Distance *  0.62137119, fetchData$Distance)

fetchDataRun <- fetchData %>%
  filter(Category == 'R') %>%
  filter(Distance > 1) %>%
  filter (Time > '00:00:00') %>%
  filter (Time < 7370) %>%
  mutate (runSeconds = seconds(Time)) %>%
  mutate (runYear = year(Date))
  
fetchDataRun$runSeconds <- as.numeric(fetchDataRun$runSeconds)
fetchDataRun$runYear <- as.factor(fetchDataRun$runYear)


ggplot(data = fetchDataRun, aes(x = Miles, y = runSeconds)) +
  geom_point(aes(colour = runYear)) +
  geom_smooth(method=lm)

ggplot(data = fetchDataRun, aes(x = Miles, y = runSeconds)) +
  geom_point() +
  geom_smooth(method=lm) +
  facet_wrap(facets = ~ runYear,nrow = 2)

ggplot(data = fetchDataRun, aes(x = Miles, y = runSeconds, colour = runYear)) +
  geom_point() +
  geom_smooth(method=lm)

runCount<-fetchDataRun %>%
  group_by(runYear) %>%
  tally()

ggplot(data = runCount, aes(x = runYear, y = n)) +
  geom_bar(aes(stat = ''))
  

