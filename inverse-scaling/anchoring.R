setwd("~/desktop/apart/blackbox-psych/")
pacman::p_load(ggplot, tidyverse)

df <- read_csv("inverse-scaling/data/anchoring_raw.csv")

df %>% 
    filter(indices == TRUE) %>%
    write_csv("inverse-scaling/data/anchoring_12.csv")

df %>%
    filter(indices == FALSE) %>%
    write_csv("inverse-scaling/data/anchoring_num.csv")

df %>%
    filter(indices && anchor_scale == 1) %>%
    write_csv("inverse-scaling/data/anchoring_12_1.csv")

df %>%
    filter(indices && anchor_scale == 0.1) %>%
    write_csv("inverse-scaling/data/anchoring_12_01.csv")

df %>%
    filter(indices && anchor_scale == 0.01) %>%
    write_csv("inverse-scaling/data/anchoring_12_001.csv")

df %>%
    filter(indices && anchor_scale == 10) %>%
    write_csv("inverse-scaling/data/anchoring_12_10.csv")

df %>%
    filter(!indices && anchor_scale == 1) %>%
    write_csv("inverse-scaling/data/anchoring_num_1.csv")

df %>%
    filter(!indices && anchor_scale == 0.1) %>%
    write_csv("inverse-scaling/data/anchoring_num_01.csv")

df %>%
    filter(!indices && anchor_scale == 0.01) %>%
    write_csv("inverse-scaling/data/anchoring_num_001.csv")

df %>%
    filter(!indices && anchor_scale == 10) %>%
    write_csv("inverse-scaling/data/anchoring_num_10.csv")

