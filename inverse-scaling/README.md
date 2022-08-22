# 📉 Inverse scaling challenge

![Badge](https://img.shields.io/static/v1?label=type&message=research&color=blue)
![Badge](https://img.shields.io/static/v1?label=status&message=in%20progress&color=orange)

Participating in the [inverse scaling challenge](https://github.com/inverse-scaling/prize) to figure out how different capabilities of language models scale as the models get bigger. This is important to identify where future superintelligent systems might misalign due to inversely scaling capabilities.

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
- [ ] Write up results
  - [x] Submit and get an inverse scaling law down on paper: **Anchoring**
  - [ ] Submit: Saliency bias
  - [ ] Submit: Conjunction fallacy
  - [ ] Submit: Political bias
  - [ ] Submit: Future bias
