library("dplyr")

data <- read.csv("msleep_ggplot2.csv")
primates <- filter(data, order=="Primates")

class(primates)
class(data)

nrow(data)
nrow(primates)


sleep <- filter(data, order=="Primates") %>% select(sleep_total)

class(sleep)

mean(unlist(sleep))

?summarise


filter(data, order=="Primates") %>% summarise(mean_val = mean(sleep_total), t=n())

install.packages("gapminder")
library(gapminder)
library(dplyr)
data(gapminder)
head(gapminder)
expVec <- filter(gapminder, year==1952) %>% select(lifeExp) %>% unlist

mean(expVec <= 60)- mean(expVec <= 40)
