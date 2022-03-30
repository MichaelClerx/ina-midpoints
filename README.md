# Variability in reported midpoints of (in)activation for cardiac INa

This repository contains the data and code accompanying the paper 

> Variability in reported midpoints of (in)activation for cardiac INa
> Michael Clerx, Someone, Someone
> Published somewhere
> DOI

The data is all derived from an sqlite database [data-in/mutations.sqlite] that was created in 2016 for the study

> Predicting changes to INa from missense mutations in human SCN5A
> Michael Clerx, Jordi Heijman, Pieter Collins, Paul G.A. Volders
> Scientific Reports
> https://doi.org/10.1038/s41598-018-30577-5
> https://github.com/MichaelClerx/mutations-scn5a

## Requirements

The database can be opened with any [SQLite](https://en.wikipedia.org/wiki/SQLite) compatible software.
The included scripts require Python 3.6 or newer, with `numpy` and `scipy` installed.
The figures can be recreated using [Veusz](https://veusz.github.io/).

## Data sources for figures and paper

### Figure 1
- CSVs generated by `f1ab-midpoints.py`
- CSVs generated by `f1cd-correlations.py`
- Counts shown by `f1ab-midpoints.py`
- Counts for myocyte experiments directly from `mutations.sqlite`
- Note that the histogram in Figure 1 is made using a series of Veusz commands that must be repeated manually (22 bins, starting at 20mV, ending at 64mV).

### Figure 2
- CSVs generated by `f1ab-midpoints.py`
- Counts (m and n) shown by `f1ab-midpoints.py`

### Table 1
- Generated by `f1ab-midpoints.py`

### Text
- Number of studies surveyed from `d1-counts.py`
- Total number of reports (1 or more per publication) of `Va` and/or `Vi` from `d1-counts.py`
- Standard deviation of `Va` (lowest, mean, highest) from `d2-sigmas.py`
- Standard deviation of `Vi` (lowest, mean, highest) from `d2-sigmas.py`
- Standard deviation of summed `Va` from `f1ab-midpoints.py`
- Number of reports of both `Va` and `Vi` shown by `f1cd-correlations.py`
- Linear regression numbers shown by `f1cd-correlations.py`
- Standard deviation of "correlation-corrected" Vi shown by `f1cd-correlations.py`
- Minimum and maximum temperatures: `d3-temperatures.py`

