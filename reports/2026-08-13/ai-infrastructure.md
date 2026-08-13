# AI Infrastructure — 2026-08-13

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [\[Roadmap\] sglang auto tuner](https://github.com/sgl-project/sglang/issues/13363)

- Project: `sgl-project/sglang`
- Tier: `maintainer-invited`
- Evidence: Maintainers marked this as a good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[Feature\] Add KV cache usage prometheus metrics](https://github.com/sgl-project/sglang/issues/5979)

- Project: `sgl-project/sglang`
- Tier: `maintainer-invited`
- Evidence: Maintainers marked this as a good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[RFC\]: Support ViT Full CUDA Graph (Tracker)](https://github.com/vllm-project/vllm/issues/38175)

- Project: `vllm-project/vllm`
- Tier: `maintainer-invited`
- Evidence: Maintainers explicitly requested help; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[core\] Ray session conflicts with PyArrow+HDFS](https://github.com/ray-project/ray/issues/36415)

- Project: `ray-project/ray`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: vllm/vllm-openai:latest fails to start Gemma4 with Transformers 5.15.0](https://github.com/vllm-project/vllm/issues/51744)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Decode Context Parallelism (`--decode-context-parallel-size`) output drift and gibberish in v0.21.0 and latest nightly](https://github.com/vllm-project/vllm/issues/41623)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [LiteLLM](https://github.com/BerriAI/litellm)

- **Release** [v1.98.0-dev.2](https://github.com/BerriAI/litellm/releases/tag/v1.98.0-dev.2) — 
- **Pull Request** [fix(azure_ai): recognize real Search doc endpoints so teams can read/write via passthrough](https://github.com/BerriAI/litellm/pull/33757) — 11 comments · 1 reactions · open
- **Pull Request** [feat(guardrails): add payload, applicability and dispatch controls to generic_guardrail_api](https://github.com/BerriAI/litellm/pull/36731) — 4 comments · 1 reactions · open
- **Pull Request** [refactor: replace Any with precise types across responses, proxy, and llms modules](https://github.com/BerriAI/litellm/pull/36763) — 4 comments · 1 reactions · open
- **Pull Request** [feat(gemini): day-0 pricing for gemini-3.7-flash](https://github.com/BerriAI/litellm/pull/36792) — 5 comments · 1 reactions · closed
- **Pull Request** [feat(guardrails/xecguard): pass the calling virtual key through xecguard to the SIEM (splunk)](https://github.com/BerriAI/litellm/pull/36797) — 4 comments · 1 reactions · open
- **Pull Request** [test(agents): assert the tuple get_agent_list now returns](https://github.com/BerriAI/litellm/pull/36216) — 3 comments · 1 reactions · closed

### [vLLM](https://github.com/vllm-project/vllm)

- **Pull Request** [\[Frontend\] Add reusable TP1 initialized-engine snapshots](https://github.com/vllm-project/vllm/pull/51360) — 9 comments · 2 reactions · open
- **Pull Request** [\[RFC\]\[Bug Fix\]\[Spec Decode\] Require explicit speculative methods](https://github.com/vllm-project/vllm/pull/51338) — 6 comments · 2 reactions · open
- **Pull Request** [Support DSpark configs with `architectures=DSparkDraftModel` + `model_type=qwen3`](https://github.com/vllm-project/vllm/pull/52197) — 2 comments · 3 reactions · open
- **Pull Request** [\[Quantization\] Remove dead `QuantizationConfig.is_mxfp4_quant`](https://github.com/vllm-project/vllm/pull/51793) — 5 comments · 2 reactions · closed
- **Pull Request** [\[ROCm\]\[Model\]\[Bugfix\] Enable GLM-5.2-MXFP4 on the deepseek_v32 path and fix sparse attention correctness](https://github.com/vllm-project/vllm/pull/51915) — 1 comments · 3 reactions · open
- **Pull Request** [\[Bugfix\] Do not require SupportsPP of draft models under pipeline parallelism](https://github.com/vllm-project/vllm/pull/52117) — 2 comments · 2 reactions · open
- **Pull Request** [\[Core\] Update PyTorch to 2.14.0, torchvision to 0.29.0, triton to 3.8.0 (test channel)](https://github.com/vllm-project/vllm/pull/52183) — 2 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\]\[Mamba2\] Fix assert crash when prefill-reclassified-as-decode occurs with no concurrent spec tokens](https://github.com/vllm-project/vllm/pull/46424) — 4 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\]\[Spec Decode\] Make EAGLE weight sharing TP-consistent](https://github.com/vllm-project/vllm/pull/50280) — 2 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\]\[LoRA\] Fix PEFT 0.18+ target_parameters LoRA loading for 3D MoE experts](https://github.com/vllm-project/vllm/pull/52198) — 1 comments · 2 reactions · open
- **Pull Request** [\[Feature\] Add local/external prefix-cache hit breakdown to prompt_tokens_details (additive)](https://github.com/vllm-project/vllm/pull/52199) — 1 comments · 2 reactions · open

### [SGLang](https://github.com/sgl-project/sglang)

- **Pull Request** [\[AMD\]\[Quantization\] Online MXFP4 quantization 4/N - NVFP4 to MXFP4 Online Requantization on AMD GPUs](https://github.com/sgl-project/sglang/pull/29328) — 22 comments · 1 reactions · open
- **Pull Request** [\[diffusion\] Support LTX-2.5](https://github.com/sgl-project/sglang/pull/34471) — 1 comments · 1 reactions · open
- **Pull Request** [Add new spec-dec support and quant recipe for Nano v3](https://github.com/sgl-project/sglang/pull/33554) — 3 comments · 0 reactions · open
- **Pull Request** [Publish per-scheduler load on a dedicated socket for load-aware routers](https://github.com/sgl-project/sglang/pull/34608) — 2 comments · 0 reactions · open
- **Pull Request** [\[PD\] Don't release KV pages while Mooncake transfers are in flight](https://github.com/sgl-project/sglang/pull/32564) — 1 comments · 0 reactions · open
- **Pull Request** [Fix Whisper transcription for audio over 30 seconds](https://github.com/sgl-project/sglang/pull/33604) — 1 comments · 0 reactions · open
- **Pull Request** [Improve M3 performance on MI350](https://github.com/sgl-project/sglang/pull/34014) — 0 comments · 0 reactions · open
- **Pull Request** [\[Cosmos3\] Add cosmos3 transfer capability](https://github.com/sgl-project/sglang/pull/34747) — 0 comments · 0 reactions · open
- **Pull Request** [feat(cli): add extensible serve backend plugins](https://github.com/sgl-project/sglang/pull/34753) — 1 comments · 0 reactions · open
- **Pull Request** [\[Cosmos3\] Add cosmos3 Reasoner to llm only inference](https://github.com/sgl-project/sglang/pull/33572) — 1 comments · 0 reactions · open

### [Ray](https://github.com/ray-project/ray)

No new or materially changed signals.

### [BentoML](https://github.com/bentoml/BentoML)

No new or materially changed signals.
