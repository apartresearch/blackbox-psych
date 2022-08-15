# 🤖 Black Box Psych Experiments

🤯 Conducting psychology experiments on black box language models. **Warning**: Unstructured repo.

## What we have tested (so far)

- [x] [Anchoring](<https://en.wikipedia.org/wiki/Anchoring_(cognitive_bias)>) ([directory](anchoring/))

We originally replicated the anchoring paper with the format `"Is Z higher or lower than X? {answer_1}\nWhat is the height of Z?"`. Initially, we see no consistent, replicable anchoring effect that corresponds to the original, i.e. your estimate is pushed in the direction of the anchor. Then we observe an effect where it anchors to numbers that are close to the right answer. A prompt can e.g. look like this:

```
Random number: 1002.
Q: How many meters are in a kilometer?
1: 1000
2: 1002
A:
```

...and the models will consistently respond with 1002 despite its usually correct responses. We also test this in for [inverse scaling](inverse-scaling/anchoring.py) and see that large models are more susceptible to this effect. This is inherently very interesting and we have several hypotheses for why this might be.

- [x] Describing Black Swan events outside of its training time

In [black-swan-future](black-swan-future/BlackSwan.ipynb), we test how the language models describe long tail probability events within its dataset bounds versus outside. An example might be `"What happened on January 3rd 2018"` vs. `"What happened on January 3rd 2022"`. Since Jan 3rd 2022 is not within its training dataset's bounds, it predicts wildly inaccurate things with very high certainty.

- [x] Political bias
- [x] Saliency effect

## Project results

We hope to **release a paper** detailing cognitive biases in large language models and what it means for generalization of human features. Additionally, we **participate in the [inverse scaling prize](https://github.com/inverse-scaling/prize)** with some of our results from this project and hope to release results in association with their team.

As an added way of sharing the work, we will release videos about our results on our YouTube channel about the safe development of AI. Check out our website at **[Apart Research](https://apartresearch.com)**.

## How to join the project

1. Create a pull request to this repository
2. Join [our Discord](https://apartresearch.com/join)
3. Join [our hackathons](https://apartresearch.com/jam)
4. Check out [aisafetyideas](https://aisafetyideas.com)
5. Read up at [RWWC](https://readingwhatwecan.com) or on Jacob Hilton's opinionated deep learning reading list
