[issue-template]: ../../../issues/new?template=BUG_REPORT.md
[feature-template]: ../../../issues/new?template=FEATURE_REQUEST.md

![singnetlogo](../../assets/singnet-logo.jpg?raw=true 'SingularityNET')

# CNTK Language Understanding

This service uses [CNTK Language Understanding](https://cntk.ai/pythondocs/CNTK_202_Language_Understanding.html)
to process text and perform slot tagging.

It is part of our [NLP Services](https://github.com/singnet/nlp-services).

### Welcome

The service receives as input multiple files of a dataset. All input files must be supplied.
The train and test dataset must be in CTF format ([link](https://docs.microsoft.com/en-us/cognitive-toolkit/brainscript-cntktextformat-reader#cntk-text-format-ctf)). 
The query and slots files are used to predict on new sentences.
Then the service must receive as input the vocabulary size, number of slots labels and number of intent labels.
With these parameters the service will be able to train its model to perform slot tagging.
As last parameter, the service receives a file with sentences (one per line).
This file will be the input of the trained model.
Finally the service returns 2 URLs, one with file containing the input sentences and slot tagging
and the second with file of the trained model.

### What’s the point?

[[SERVICE_DOCS_WHATS_THE_POINT]]

### How does it work?

[[SERVICE_DOCS_HOW_DOES_IT_WORK]]

You can use this service from [SingularityNET DApp](http://beta.singularitynet.io/).

You can also call the service from SingularityNET CLI (`snet`).

Assuming that you have an open channel (`id: 0`) to this service:

```
$ snet client call 0 0.00000001 54.203.198.53:7075 slot_tagging '{"train_ctf_url": "https://github.com/Microsoft/CNTK/blob/release/2.6/Tutorials/SLUHandsOn/atis.train.ctf?raw=true", "test_ctf_url": "https://github.com/Microsoft/CNTK/blob/release/2.6/Tutorials/SLUHandsOn/atis.test.ctf?raw=true", "query_wl_url": "https://github.com/Microsoft/CNTK/blob/release/2.6/Examples/LanguageUnderstanding/ATIS/BrainScript/query.wl?raw=true", "slots_wl_url": "https://github.com/Microsoft/CNTK/blob/release/2.6/Examples/LanguageUnderstanding/ATIS/BrainScript/slots.wl?raw=true", "intent_wl_url": "https://github.com/Microsoft/CNTK/blob/release/2.6/Examples/LanguageUnderstanding/ATIS/BrainScript/intent.wl?raw=true", "vocab_size": 943, "num_labels": 129, "num_intents": 26, "sentences_url": "http://54.203.198.53:7000/LanguageUnderstanding/CNTK/Example/sentences.txt"}'
unspent_amount_in_cogs before call (None means that we cannot get it now):1

response:
output URL: http://54.203.198.53:7000/LanguageUnderstanding/CNTK/Output/684bb98e0ef1537c1b7d.txt
model  URL: http://54.203.198.53:7000/LanguageUnderstanding/CNTK/Output/684bb98e0ef1537c1b7d.model
```

The output format is:
 - `output URL`: URL of the service's output file.
 - `model URL`: URL of the trained model file.

### What to expect from this service?

Input:

 - `gRPC method`: slot_tagging.
 - `train_ctf_url`: "https://github.com/Microsoft/CNTK/blob/release/2.6/Tutorials/SLUHandsOn/atis.train.ctf?raw=true".
 - `test_ctf_url`: "https://github.com/Microsoft/CNTK/blob/release/2.6/Tutorials/SLUHandsOn/atis.test.ctf?raw=true".
 - `query_wl_url`: "https://github.com/Microsoft/CNTK/blob/release/2.6/Examples/LanguageUnderstanding/ATIS/BrainScript/query.wl?raw=true".
 - `slots_wl_url`: "https://github.com/Microsoft/CNTK/blob/release/2.6/Examples/LanguageUnderstanding/ATIS/BrainScript/slots.wl?raw=true".
 - `intent_wl_url`: "https://github.com/Microsoft/CNTK/blob/release/2.6/Examples/LanguageUnderstanding/ATIS/BrainScript/intent.wl?raw=true".
 - `vocab_size`: 943.
 - `num_labels`: 129.
 - `num_intents`: 26.
 - `sentences_url`: "http://54.203.198.53:7000/LanguageUnderstanding/CNTK/Example/sentences.txt".

Response:

```
response:
output URL: http://54.203.198.53:7000/LanguageUnderstanding/CNTK/Output/684bb98e0ef1537c1b7d.txt
model  URL: http://54.203.198.53:7000/LanguageUnderstanding/CNTK/Output/684bb98e0ef1537c1b7d.model
```

Sentences file input content:
```
BOS flights from new york to seattle by delta airlines EOS
BOS departures from los angeles to san diego EOS
BOS i want to book a flight from miami to atlanta by american airlines EOS
```

Output file content:
```
0: BOS flights from new york to seattle by delta airlines EOS
0: [('BOS', 'O'), ('flights', 'O'), ('from', 'O'), ('new', 'B-fromloc.city_name'), ('york', 'I-fromloc.city_name'), ('to', 'O'), ('seattle', 'B-toloc.city_name'), ('by', 'O'), ('delta', 'B-airline_name'), ('airlines', 'I-airline_name'), ('EOS', 'O')]
1: BOS departures from los angeles to san diego EOS
1: [('BOS', 'O'), ('departures', 'O'), ('from', 'O'), ('los', 'B-fromloc.city_name'), ('angeles', 'I-fromloc.city_name'), ('to', 'O'), ('san', 'B-toloc.city_name'), ('diego', 'I-toloc.city_name'), ('EOS', 'O')]
2: BOS i want to book a flight from miami to atlanta by american airlines EOS
2: [('BOS', 'O'), ('i', 'O'), ('want', 'O'), ('to', 'O'), ('book', 'O'), ('a', 'O'), ('flight', 'O'), ('from', 'O'), ('miami', 'B-fromloc.city_name'), ('to', 'O'), ('atlanta', 'B-toloc.city_name'), ('by', 'O'), ('american', 'B-airline_name'), ('airlines', 'I-airline_name'), ('EOS', 'O')]
```

Input:

 - `gRPC method`: intent.
 - `train_ctf_url`: "https://github.com/Microsoft/CNTK/blob/release/2.6/Tutorials/SLUHandsOn/atis.train.ctf?raw=true".
 - `test_ctf_url`: "https://github.com/Microsoft/CNTK/blob/release/2.6/Tutorials/SLUHandsOn/atis.test.ctf?raw=true".
 - `query_wl_url`: "https://github.com/Microsoft/CNTK/blob/release/2.6/Examples/LanguageUnderstanding/ATIS/BrainScript/query.wl?raw=true".
 - `slots_wl_url`: "https://github.com/Microsoft/CNTK/blob/release/2.6/Examples/LanguageUnderstanding/ATIS/BrainScript/slots.wl?raw=true".
 - `intent_wl_url`: "https://github.com/Microsoft/CNTK/blob/release/2.6/Examples/LanguageUnderstanding/ATIS/BrainScript/intent.wl?raw=true".
 - `vocab_size`: 943.
 - `num_labels`: 129.
 - `num_intents`: 26.
 - `sentences_url`: "http://54.203.198.53:7000/LanguageUnderstanding/CNTK/Example/sentences.txt".

Response:

```
response:
output URL: http://54.203.198.53:7000/LanguageUnderstanding/CNTK/Output/684bb98e0ef1537c1b7d.txt
model  URL: http://54.203.198.53:7000/LanguageUnderstanding/CNTK/Output/684bb98e0ef1537c1b7d.model
```

Sentences file input content:
```
BOS flights from new york to seattle by delta airlines EOS
BOS how much is the ticket to washington from san francisco EOS
BOS departures from los angeles to san diego EOS
BOS what is the name of the main airport in chicago EOS
BOS i want to book a flight from miami to atlanta by american airlines EOS
```

Output file content:
```
0: BOS flights from new york to seattle by delta airlines EOS -> flight
1: BOS how much is the ticket to washington from san francisco EOS -> airfare
2: BOS departures from los angeles to san diego EOS -> flight
3: BOS what is the name of the main airport in chicago EOS -> airport
4: BOS i want to book a flight from miami to atlanta by american airlines EOS -> flight
```