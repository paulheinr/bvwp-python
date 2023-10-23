# Calculation of Emissions

This project scrapes data from the official website of BVWP and analyzes them.

## How to run

You can run each of these files in `bvwp-emissions`:

* `all_emissions`
* `co2`
* `rail`

You can pass the output file path as parameter.

## TODO

### Refactoring

- [ ] Generalize soup value extraction
- [ ] Street: generalize postprocessing
- [ ] Understand the difference between `all_emissions` and `co2` (I guess there is no except `co2` adds more
  calculation)

### Regression Testing

- [x] Rail
- [ ] Street emissions (For now, there are added a few projects and some calculated numbers are wrong.)
- [ ] Make regression tests work automatically


