# how-to-extract-structured-data-with-llms


## Introduction 

Information is often much easier to reuse and analyze when it is in structured form, i.e., when different samples are characterized by the same, so-called data schema. 
A data schema describes form data in which data should be structured, for example, which attributes one uses to characterize an experiment, simulation, or chemical. 

- Structured knowledge also allows precise querying 
- Curation of existing knowledge databases is currently mostly done with a lot of human effort 
- A lot of knowledge, however, is communicated in natural language. 

### Why LLMs? 

The motivation for using LLMs in this task is that it might be easier to customize 

## Prior work 
- paper QA
- Ceder group 
	- https://arxiv.org/abs/2212.05238 
- Luc/Guillaume https://chemrxiv.org/engage/api-gateway/chemrxiv/assets/orp/resource/item/65570cb1dbd7c8b54b6ff36b/original/automatic-extraction-of-fair-data-from-publications-using-llm.pdf
- https://arxiv.org/pdf/2308.01727.pdf
- https://arxiv.org/pdf/2309.10952.pdf 
- https://arxiv.org/abs/2310.03666 
- https://arxiv.org/abs/2309.17169
- [[SPIRES]] https://arxiv.org/abs/2304.02711 https://www.youtube.com/watch?v=z38lI6WyBsY  https://github.com/monarch-initiative/ontogpt 
	- [[Structured prompt interrogation and recursive extraction of semantics (SPIRES) - A method for populating knowledge bases using zero-shot learning]]
- https://arxiv.org/pdf/2307.16648.pdf 
	- [[LLMs4OL Large Language Models for Ontology Learning]]
- https://arxiv.org/pdf/2308.02357v1.pdf
- https://aclanthology.org/2023.acl-long.868.pdf 
- https://github.com/Kedar-Materials-by-Design-Lab/Harnessing-GPT-3.5-for-Text-Parsing-in-Solid-State-Synthesis-case-study-of-ternary-chalchogenides
- GPT NER https://arxiv.org/abs/2304.10428 
- https://arxiv.org/pdf/2304.09433.pdf
- https://neo4j.com/developer-blog/construct-knowledge-graphs-unstructured-text/
- https://xebia.com/blog/archetype-llm-batch-use-case/
- https://artificialcorner.com/introducing-patentgpt-a-tool-for-extracting-technical-measurements-from-patents-80fa30c2bbd7 
	- https://github.com/arminnorouzi/patentGPT?source=post_page-----80fa30c2bbd7-------------------------------- 
- https://www.youtube.com/watch?v=xZzvwR9jdPA
- https://eyurtsev.github.io/kor/index.html
- Zero shot phenotype https://www.nature.com/articles/s41746-023-00957-x
- GPT-4 vision:
	- https://jschrier.github.io/blog/2023/12/06/GPT-4-vision-preview-for-scientific-image-processing-The-Bad,-The-Mediocre,-and-the-Tolerable.html
	- https://arxiv.org/abs/2312.05468
- Mohamad https://arxiv.org/abs/2312.11690
- [[Christopher J. Mungall]] http://arxiv.org/abs/2312.10904 


Include different examples in paper: 
- GPT API with tools 
- Guidance
- LLM with prompt 
- JSONformer 

Select one paper and get the desired schema. 

### Alternative approaches

- Jacqueline Cole’s work

### For images
- webplotdigitizer 
- other specialized models https://link.springer.com/article/10.1007/s10032-022-00424-5

## Data extraction tasks 

### [[NER ]]
- identify spans mentioning relevant entities 

### Relation extraction 
- extract triples: links entities via predicates

### Open Information Extraction

### Entity Linking

### Relation Linking
### Ontology learning
- term typing 
- taxonomy discovery
- extraction of non-taxonomic relations

### Classification 

[[Coreference resolution]] expressions that refer to the same entity  


## Workflow 

### OCR 

- Nougat 
- https://github.com/VikParuchuri/marker 
- conventional OCR

#### Layout encoding 
- correct analysis might require understanding of the layout
- Ordering of blocks if you have multiple blocks

### Chunking documents 

https://www.youtube.com/watch?v=QpRTdZDR4tE

- Docugami

LLMs have a finite context window. Hence, we cannot provide an unlimited amount of text to the model (e.g. 2048 tokens for GPT-4). That is, we can only provide subsets, e.g. parts of a paper. This raises the natural question on how one should select the subsets.

- Vector store needed? 
	- Either you chunk or do retrieval on the fly https://x.com/jerryjliu0/status/1709343094582452634?s=20
- Chunking considerations: https://www.pinecone.io/learn/chunking-strategies/


#### Basic approaches
Toolks like NLTK can be used to split text into sentences. This ensures that chunks don’t break sentences. However, it can be more meaningful to split by paragrams as paragphs typically represent distinct ideas.

#### Advances approaches

It can be useful to have overlap between chunks: 
- context preservation (surrounding text needed to understand passage)
- smoothing transition 

More advances is semantic splitting, which splits text at semantically meaningful points. 

ChunkBert: https://arxiv.org/abs/2310.20558

Use sessiosn 



### Finetune or not finetune? How to make models follow this task

- “Old fashioned” finetuning Howard and Ruder
- Prompt tuning/prefix tuning 
- Currently, most examples use few-shot prompts (https://twitter.com/goodside/status/1564437905497628674, https://twitter.com/eugeneyan/status/1636366239873515521)

Distill OpenAI using something like https://docs.openpipe.ai/getting-started/openpipe-sdk


### Enforcing valid syntax

- https://www.llmparser.com/: 
	- Prompts to generate a certain schema 
	- Prompts to return confidence
- [[jsonformer]]
- Grammar decoding/Constrained generation: 
	- [[Guidance]] https://github.com/guidance-ai/guidance 
- OpenAI function calling 
	- [[funcchain]] Very pythonic way to use them: https://github.com/shroominic/funcchain
- Guardrails: https://docs.guardrailsai.com/ 
### Data cleanup/curation 


### Metrics 

- MAP@K: mean average precision at K 
- Precision
- Recall
- F1

All as micro/macro averagges

#### Benchmarks 

- BC5CDR (chemical-induces-disease, [[CID]] [[triples]])
- [[LLMs4OL Large Language Models for Ontology Learning]] introduced one for ontology learning 
- TEXT2KGBENCH
	- Generate KG given text and ontology 
	- Wikidata-TekGen with 10 ontologies and 13,474 sentences aligned to triples and (b) DBpedia-WebNLG with 19 ontologies and 4,860 sentences aligned to triples by reusing TekGen [Agarwal et al., 2021] and WebNLG [Gardent et al., 2017] corpora.
	- Define seven metrics 
- VRDU 
- CORD


## Multimodality


## Localization 

## Sanity checks

- Luc checks number of hydrogens 

