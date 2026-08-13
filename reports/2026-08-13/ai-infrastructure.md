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

### [\[Bug\]: upgrade vllm from 0.26.0 to 0.27.0 run deepseek v4 flash error](https://github.com/vllm-project/vllm/issues/51758)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [LiteLLM](https://github.com/BerriAI/litellm)

- **Pull Request** [feat(asqav): optional cloud signing via the agent sign endpoint](https://github.com/BerriAI/litellm/pull/31100) — 21 comments · 1 reactions · closed
- **Pull Request** [fix: allow vllm GET passthrough by checking model in query params](https://github.com/BerriAI/litellm/pull/22104) — 14 comments · 1 reactions · closed
- **Pull Request** [feat(proxy): serve Anthropic-native /v1/models for Claude Code gateway discovery](https://github.com/BerriAI/litellm/pull/35455) — 5 comments · 3 reactions · open
- **Issue** [\[Bug\]: gen_ai.system still reaches OTel exporter as 'None' in metrics/events paths — PR #26713 only fixed the span-attribute call site](https://github.com/BerriAI/litellm/issues/36759) — 2 comments · 0 reactions · open
- **Pull Request** [fix(mcp): expose client HTTP headers to logging callbacks and hooks](https://github.com/BerriAI/litellm/pull/36724) — 6 comments · 1 reactions · open
- **Issue** [\[Bug\]: Unable to reset user max budget to unlimited](https://github.com/BerriAI/litellm/issues/32474) — 4 comments · 0 reactions · open
- **Issue** [OpenTelemetry: attributes written to ended parent_span — guard checks hasattr(set_status) instead of is_recording()](https://github.com/BerriAI/litellm/issues/36746) — 1 comments · 0 reactions · open
- **Issue** [OpenAPI→MCP tool generation drops request body schema when it uses $ref (FastAPI/Pydantic specs)](https://github.com/BerriAI/litellm/issues/36765) — 1 comments · 0 reactions · open
- **Issue** [\[Bug\]: Bedrock Converse streaming emits a trailing empty chunk after the finish_reason chunk (regression in v1.94.0, PR #32255)](https://github.com/BerriAI/litellm/issues/36767) — 1 comments · 0 reactions · open
- **Issue** [\[Bug\]: /v1/chat/completions stream: response.failed becomes HTTP 200 + empty finish_reason=stop (fallbacks never run)](https://github.com/BerriAI/litellm/issues/36768) — 1 comments · 0 reactions · open
- **Pull Request** [fix(model-edit): clear a litellm param when it is removed in the editor](https://github.com/BerriAI/litellm/pull/36684) — 4 comments · 1 reactions · open
- **Pull Request** [fix(ui): add nvidia riva to the model provider list](https://github.com/BerriAI/litellm/pull/36769) — 5 comments · 1 reactions · open
- **Pull Request** [fix(bedrock): route knowledge base ingestion to control plane](https://github.com/BerriAI/litellm/pull/36771) — 4 comments · 1 reactions · open
- **Pull Request** [fix: allow vllm GET passthrough by checking model in query params](https://github.com/BerriAI/litellm/pull/36772) — 5 comments · 1 reactions · open
- **Issue** [\[Bug\]: `end_user` in SpendLogs is pinned to the first request's `user` for all subsequent requests on a shared virtual key (regression in v1.87.0)](https://github.com/BerriAI/litellm/issues/31441) — 3 comments · 0 reactions · open
- **Pull Request** [fix(utils): register_model with an empty payload silently turns unknown-model cost errors into $0.0](https://github.com/BerriAI/litellm/pull/36561) — 3 comments · 1 reactions · open
- **Pull Request** [fix(proxy): route blocked models through healthy fallbacks](https://github.com/BerriAI/litellm/pull/36672) — 2 comments · 1 reactions · open
- **Pull Request** [fix(streaming): dict-usage arm drops prompt_tokens_details/completion_tokens_details its sibling arms preserve](https://github.com/BerriAI/litellm/pull/36678) — 3 comments · 1 reactions · open
- **Pull Request** [refactor: replace Any with precise types across responses, proxy, and llms modules](https://github.com/BerriAI/litellm/pull/36763) — 3 comments · 1 reactions · open
- **Pull Request** [fix(router): apply default priority to scheduled requests](https://github.com/BerriAI/litellm/pull/36780) — 6 comments · 1 reactions · closed
- **Issue** [\[Bug\]: default_priority not being used when no priority provided](https://github.com/BerriAI/litellm/issues/36774) — 1 comments · 0 reactions · open
- **Pull Request** [feat(models): refresh GitHub Copilot pricing and metadata](https://github.com/BerriAI/litellm/pull/32762) — 5 comments · 1 reactions · open
- **Pull Request** [fix: resolve zero token usage in Google GenAI adapter streaming path](https://github.com/BerriAI/litellm/pull/33050) — 4 comments · 1 reactions · open
- **Pull Request** [fix(vertex batches): reject vertex_location='global' up front](https://github.com/BerriAI/litellm/pull/35366) — 5 comments · 1 reactions · open
- **Pull Request** [fix(proxy): guard optional prisma import in DB exception classifiers](https://github.com/BerriAI/litellm/pull/35458) — 4 comments · 1 reactions · open
- **Pull Request** [fix(proxy): preserve repeated multipart form fields in get_form_data](https://github.com/BerriAI/litellm/pull/36271) — 5 comments · 1 reactions · open
- **Pull Request** [feat(azure_ai): shape FW-Kimi / Kimi like Moonshot for Foundry](https://github.com/BerriAI/litellm/pull/36773) — 4 comments · 1 reactions · closed
- **Pull Request** [feat(guardrails): add new upstream presidio pii entities including german set](https://github.com/BerriAI/litellm/pull/36775) — 5 comments · 1 reactions · open
- **Pull Request** [feat(ui): add user ID request log filter](https://github.com/BerriAI/litellm/pull/36781) — 3 comments · 1 reactions · open
- **Pull Request** [fix(bedrock): drop trailing empty Converse chunk](https://github.com/BerriAI/litellm/pull/36783) — 2 comments · 1 reactions · open

### [vLLM](https://github.com/vllm-project/vllm)

- **Pull Request** [\[New Model\]\[Nvidia\] Add SM12x support for DeepSeek V4 Flash with essential fixes](https://github.com/vllm-project/vllm/pull/41834) — 441 comments · 40 reactions · open
- **Pull Request** [Add Muse Glimmer model support](https://github.com/vllm-project/vllm/pull/51655) — 34 comments · 16 reactions · open
- **Pull Request** [\[Kimi-K3\] Add GEMM-RS for sequence parallelism](https://github.com/vllm-project/vllm/pull/52079) — 8 comments · 3 reactions · closed
- **Issue** [\[Bug\]: vllm/vllm-openai:latest fails to start Gemma4 with Transformers 5.15.0](https://github.com/vllm-project/vllm/issues/51744) — 14 comments · 5 reactions · open
- **Pull Request** [\[Bugfix\] Add Kimi K3 MoE support to benchmark_moe.py](https://github.com/vllm-project/vllm/pull/50082) — 4 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Add DeepseekV4ForCausalLM to benchmark_moe.py model param dispatch](https://github.com/vllm-project/vllm/pull/52048) — 3 comments · 2 reactions · closed
- **Pull Request** [\[LoRA\]\[Gemma4\] Support vision tower LoRA](https://github.com/vllm-project/vllm/pull/42662) — 17 comments · 4 reactions · closed
- **Pull Request** [\[ROCm\] Defer `tilelang` import through its import `from vllm.tilelang_utils import tilelang` and relaxed `has_tilelang`](https://github.com/vllm-project/vllm/pull/51159) — 25 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Restore multimodal support on the plain "vllm" throughput backend](https://github.com/vllm-project/vllm/pull/52168) — 0 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Fix MiniMax M3 prompt reasoning initialization](https://github.com/vllm-project/vllm/pull/50594) — 22 comments · 2 reactions · open
- **Issue** [\[Performance\]: Improve Pixtral vision attention scaling for batched images](https://github.com/vllm-project/vllm/issues/52180) — 0 comments · 0 reactions · open
- **Pull Request** [buffer size insuffient Dspark sd for FlashInfer MNNVL allreduce](https://github.com/vllm-project/vllm/pull/50932) — 21 comments · 2 reactions · open
- **Pull Request** [\[Kernel\]\[Perf\] Add fused CUDA post-conv MTP decode kernel for Qwen3.5 GDN](https://github.com/vllm-project/vllm/pull/51674) — 9 comments · 5 reactions · open
- **Pull Request** [\[5/N\]\[KV-Cache Layout Refactor\] Backend-published KV packing via customize_spec](https://github.com/vllm-project/vllm/pull/51704) — 21 comments · 2 reactions · open
- **Pull Request** [\[K3\] support recoverssm for K3](https://github.com/vllm-project/vllm/pull/51855) — 1 comments · 2 reactions · open
- **Pull Request** [Add vllm_enable_compile_cache config flag with backward compatibility](https://github.com/vllm-project/vllm/pull/33763) — 19 comments · 2 reactions · open
- **Issue** [\[ROCm\]\[AMD\] Kimi-K3 Gap and Roadmap Tracking](https://github.com/vllm-project/vllm/issues/50682) — 16 comments · 0 reactions · open
- **Pull Request** [\[Frontend\] Move api_server.py out openai folder](https://github.com/vllm-project/vllm/pull/52131) — 1 comments · 0 reactions · open
- **Pull Request** [fused_moe: add VLLM_TRITON_USE_TD tensor-descriptor path](https://github.com/vllm-project/vllm/pull/42436) — 10 comments · 4 reactions · closed
- **Pull Request** [\[Bugfix\] Keep Qwen3Next layer boundaries sequence parallel](https://github.com/vllm-project/vllm/pull/50685) — 11 comments · 3 reactions · open
- **Issue** [\[Feature\]:\[New Model\] Gemma4UnifiedForConditionalGeneration (google/gemma-4-12B-it)](https://github.com/vllm-project/vllm/issues/46967) — 1 comments · 4 reactions · closed
- **Issue** [\[Bug\] v0.27.0 engine permanently stalls after ~1 min idle on 4-node TP=4 (GB10/sm_121, aarch64): shm_broadcast writer starves, requests never reach scheduler](https://github.com/vllm-project/vllm/issues/51921) — 10 comments · 0 reactions · open
- **Pull Request** [\[Bugfix\]\[CPU\] Enable C++ causal_conv1d GDN path and float32 SSM cache on non-AMX AVX-512BF16 CPUs](https://github.com/vllm-project/vllm/pull/49688) — 6 comments · 3 reactions · open
- **Pull Request** [\[ROCm\]\[AMD\]\[Installation\] add LMCache kv-connector installation and runtime packages to docker image](https://github.com/vllm-project/vllm/pull/51208) — 6 comments · 3 reactions · open
- **Pull Request** [\[1/N\] HiSparse: host-resident sparse-MLA decode hot-buffering](https://github.com/vllm-project/vllm/pull/51323) — 10 comments · 2 reactions · open
- **Pull Request** [\[MoE\] Refine FlashInfer one-sided All2All integration](https://github.com/vllm-project/vllm/pull/51924) — 7 comments · 3 reactions · open
- **Issue** [\[RFC\]: Extended online quantization roadmap](https://github.com/vllm-project/vllm/issues/52167) — 1 comments · 2 reactions · open
- **Pull Request** [\[Model Runner V2\]\[Spec Decode\] Support spec decode with draft model](https://github.com/vllm-project/vllm/pull/43091) — 9 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Fix `--data-parallel-start-rank 0` being treated as unset in `create_engine_config`](https://github.com/vllm-project/vllm/pull/47692) — 8 comments · 2 reactions · closed
- **Pull Request** [\[Refactor\]: StructuredOutputManager x Speculative Decoding Refactor](https://github.com/vllm-project/vllm/pull/48200) — 5 comments · 3 reactions · open

### [SGLang](https://github.com/sgl-project/sglang)

- **Issue** [\[Tracking\] CI Test Failures and Fixes](https://github.com/sgl-project/sglang/issues/17050) — 13 comments · 10 reactions · open
- **Issue** [CUDA Coredump Tracker](https://github.com/sgl-project/sglang/issues/26340) — 233 comments · 0 reactions · open
- **Pull Request** [\[DSv4\] Integrate TRT-LLM DSv4 Attention for SM100/103](https://github.com/sgl-project/sglang/pull/30805) — 37 comments · 0 reactions · open
- **Issue** [\[RFC\] Position-Independent KV Cache Reuse for Agentic/RAG Workloads](https://github.com/sgl-project/sglang/issues/30928) — 12 comments · 4 reactions · open
- **Pull Request** [\[FlashInfer v0.6.16\] Support FlashInfer CuTe DSL NVFP4 MoE quantization](https://github.com/sgl-project/sglang/pull/28354) — 29 comments · 0 reactions · open
- **Pull Request** [\[AMD\] Add fused all-reduce RMSNorm per-token FP8/MXFP4 quant](https://github.com/sgl-project/sglang/pull/29723) — 15 comments · 2 reactions · open
- **Pull Request** [Profiling Enhancements \[2/3\]: detailed execution step annotations](https://github.com/sgl-project/sglang/pull/24911) — 10 comments · 1 reactions · open
- **Pull Request** [\[AMD\] \[Docker\] Upgrade Python 3.12 + torch 2.11 + triton 3.7 in ROCm 7.2.4](https://github.com/sgl-project/sglang/pull/30984) — 15 comments · 0 reactions · open
- **Pull Request** [\[DSA\] Add LiteTopk fused indexer top-k prefill path for SM100](https://github.com/sgl-project/sglang/pull/32094) — 6 comments · 2 reactions · open
- **Pull Request** [\[AMD\] Add dense-FP8 for MXFP4 checkpoints with fused silu, mul, activation quant](https://github.com/sgl-project/sglang/pull/28932) — 13 comments · 0 reactions · open
- **Pull Request** [\[AMD\] Enable gfx1250 Support](https://github.com/sgl-project/sglang/pull/32754) — 12 comments · 1 reactions · open
- **Pull Request** [\[AMD\] Optimize KIMI-K3 with Triton MLA decode kernel by tuning the stage-1 geometry for gfx950](https://github.com/sgl-project/sglang/pull/34580) — 4 comments · 2 reactions · open
- **Issue** [SGLang not support hidden_size=4096, moe_intermediate_size=2048  MoE](https://github.com/sgl-project/sglang/issues/30595) — 2 comments · 0 reactions · open
- **Pull Request** [add fid accuracy benchmark for sglang diffusion t2i model](https://github.com/sgl-project/sglang/pull/25871) — 6 comments · 1 reactions · open
- **Pull Request** [\[NPU\] Add mxfp4-w4a8 MOE Quantization Support for NPU](https://github.com/sgl-project/sglang/pull/30318) — 11 comments · 0 reactions · open
- **Pull Request** [\[XPU\] upgrade sglang xpu backend to PyTorch 2.13](https://github.com/sgl-project/sglang/pull/31751) — 7 comments · 0 reactions · open
- **Pull Request** [\[DeepSeek-V4\] Add Q8KV8 sparse MLA prefill runtime backend](https://github.com/sgl-project/sglang/pull/32327) — 3 comments · 1 reactions · open
- **Pull Request** [kernel: port CUTLASS fp8_scaled_mm to JIT and expand SM120 M tiles](https://github.com/sgl-project/sglang/pull/33216) — 2 comments · 1 reactions · open
- **Pull Request** [\[Test\] Add unit tests for reasoning_parser (Apertus2509/CohereCommand4 & ReasoningParser)](https://github.com/sgl-project/sglang/pull/34493) — 2 comments · 1 reactions · open
- **Pull Request** [fix(diffusion): unshard FSDP root group for custom encoder entry points](https://github.com/sgl-project/sglang/pull/34575) — 6 comments · 0 reactions · closed
- **Issue** [\[Bug\] fa3 backend slow with mla page-size 64 for H20](https://github.com/sgl-project/sglang/issues/31310) — 1 comments · 0 reactions · open
- **Pull Request** [\[DSV4\] Fix SWA state pool over-allocation by using storage page size instead of model window](https://github.com/sgl-project/sglang/pull/30371) — 1 comments · 1 reactions · open
- **Pull Request** [\[NPU\] \[Diffusion\] support distributed inference pipeline for GLM-Image](https://github.com/sgl-project/sglang/pull/31320) — 0 comments · 1 reactions · open
- **Pull Request** [\[Mooncake\] Fix silent SSD offload corruption when TP/PP ranks share ssd_offload_path](https://github.com/sgl-project/sglang/pull/31926) — 1 comments · 2 reactions · open
- **Pull Request** [\[Perf\] Skip trivial DSV4 nonpaged indexer logits](https://github.com/sgl-project/sglang/pull/33857) — 5 comments · 0 reactions · open
- **Pull Request** [\[AMD\]\[Spec\] Accelerate Qwen3.5 verification with grouped-head shared KV](https://github.com/sgl-project/sglang/pull/34517) — 4 comments · 0 reactions · open
- **Pull Request** [\[Fix\] Fix Qwen3.5 MTP startup with HiCache](https://github.com/sgl-project/sglang/pull/34560) — 4 comments · 0 reactions · open
- **Pull Request** [\[AMD\] CI: drop the spaces from SGL_EVAL_SPEC (fixes ROCm 7.2 stage-a sgl-eval install)](https://github.com/sgl-project/sglang/pull/34689) — 5 comments · 0 reactions · open
- **Pull Request** [Retain SWA down to the last state checkpoint](https://github.com/sgl-project/sglang/pull/34729) — 5 comments · 0 reactions · open
- **Pull Request** [\[AMD\] Fix Triton 3.7 gfx950 extend-attention spills](https://github.com/sgl-project/sglang/pull/34741) — 0 comments · 1 reactions · open

### [Ray](https://github.com/ray-project/ray)

- **Pull Request** [serve: expose multiplexed model IDs in ReplicaDetails](https://github.com/ray-project/ray/pull/65370) — 3 comments · 1 reactions · open
- **Pull Request** [\[Data\] Add support for writing ORC files](https://github.com/ray-project/ray/pull/65453) — 1 comments · 1 reactions · open
- **Pull Request** [\[doc\] Record what blocks lifting the setuptools ceiling and replacing sphinxcontrib-redoc](https://github.com/ray-project/ray/pull/65459) — 1 comments · 1 reactions · closed
- **Pull Request** [\[doc\] Render the Jobs API spec with sphinxcontrib-openapi instead of ReDoc](https://github.com/ray-project/ray/pull/65460) — 0 comments · 1 reactions · open
- **Pull Request** [\[doc\] llms.txt: tell agents the page links also serve Markdown](https://github.com/ray-project/ray/pull/65461) — 0 comments · 1 reactions · open

### [BentoML](https://github.com/bentoml/BentoML)

No new or materially changed signals.
