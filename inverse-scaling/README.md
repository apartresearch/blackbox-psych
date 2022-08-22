# 📉 Inverse scaling challenge

## TODO

- [x] Test anchoring
  - [x] Create test suite generation
  - [x] Test in the 1000s
  - [x] Test in the 1s
  - [x] Test in the 10s
  - [x] Test in the 100s
  - [x] Test one-shot
  - [x] Test few-shot
- [ ] Saliency bias
  - [x] Test inverse scaling: **Success**
  - [x] Bug fix
  - [x] Test bug fix
  - [ ] Investigate why
  - [ ] Rerun updated dataset
- [ ] Conjunction fallacy
  - [x] Test for inverse scaling
  - [x] See why "accountant" seems to be the only good inverse scaler --> no obvious reason, another version has no inverse scaling
  - [ ] Rewrite some prompts and rerun the models
- [ ] Test prediction certainty
  - [x] How certainly does the model predict wrongly outside its training data range
  - [x] Test past / future framing
  - [ ] Possibly interesting: Rerun with new, _more probable_, questions
- [x] Test political bias
- [x] Write up results
  - [x] Get an inverse scaling law down on paper
