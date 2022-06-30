# blackbox-psych
Conducting psychology experiments on black box language models

## What we have tested (so far)
- [ ] [Anchoring](https://en.wikipedia.org/wiki/Anchoring_(cognitive_bias))

## Datasheet Anchoring
Format of the output. The ones with filename = "yes" can also be stored in the filename (e.g. `gpt-j-6b_chicago.csv`)
Column Name | Description| Example | In filename
--- | --- | --- | ---
`id` | Unique identifier per row | 1 | No
`model_name` | The model used | "gpt-j-6b" | Yes 
`temperature` | Temperature | 0.9| No
`anchor` | One of "Control", "Low", "High" | "High" | No
`anchor_val` | Value of the anchor | 20000 | No
`question_group` | Identifier for the question | "Chicago" (or "everest") | Yes
`output` | The numeric value of the model | 8489 | No