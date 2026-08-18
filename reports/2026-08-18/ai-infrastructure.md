# AI Infrastructure — 2026-08-18

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [\[Bug\]: ModelOpt Llama-4 Checkpoints Take 5+ minutes to load](https://github.com/vllm-project/vllm/issues/31624)

- Project: `vllm-project/vllm`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: help wanted, good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[Perf\]\[Kernel\] Adopt PTX 9.4 `ldmatrix.s8.s4` (hardware INT4→INT8 expanding load) in W4A8-INT8 paths](https://github.com/vllm-project/vllm/issues/49529)

- Project: `vllm-project/vllm`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[Bug\]: vllm/vllm-openai:latest fails to start Gemma4 with Transformers 5.15.0](https://github.com/vllm-project/vllm/issues/51744)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Budget enforcement bypassed in v1.82.3 for key/user max_budget despite spend exceeding max_budget](https://github.com/BerriAI/litellm/issues/26672)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Qwen3.5 CUDA Illegal Memory Access in GDN Kernel](https://github.com/vllm-project/vllm/issues/34948)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Docs mention litellm.turn_on_message_logging, which doesn't exist](https://github.com/BerriAI/litellm/issues/37143)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Documentation-related issue with no assignee listed
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Doc\]: vLLM's default NIXL connector is ~100× slower than the push connector on non-RDMA hardware, and the fix is undocumented](https://github.com/vllm-project/vllm/issues/52607)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Documentation-related issue with no assignee listed
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]:  vLLM v1 with prefix caching: first request differs from subsequent identical requests at temperature=0](https://github.com/vllm-project/vllm/issues/40896)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Prompt Injection Detection Issues](https://github.com/BerriAI/litellm/issues/19499)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Feature\]: Support time-based / peak-offpeak pricing for model cost calculation](https://github.com/BerriAI/litellm/issues/31606)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned enhancement with community reactions
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Gemma-4 fails when forcing FLASHINFER attention backend on Blackwell SM120 (head_size not supported)](https://github.com/vllm-project/vllm/issues/40677)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: 4 B200 GPU ，DP 4 + EP（or TP 4 + EP），Deepseek V4 Flash 0731 , simultaneously processing hundreds of text extraction tasks, outputting garbled characters.](https://github.com/vllm-project/vllm/issues/52404)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]:  Kimi-K3 CUDA graph capture silently corrupts output at batch=1; three distinct failure modes across cudagraph modes.](https://github.com/vllm-project/vllm/issues/52531)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [LiteLLM](https://github.com/BerriAI/litellm)

- **Issue** [\[Feature\]: Add provider Sglang](https://github.com/BerriAI/litellm/issues/13681) — 7 comments · 15 reactions · closed
- **Issue** [\[Bug\]: AnthropicException 400 - vector_store_ids: Extra inputs are not permitted](https://github.com/BerriAI/litellm/issues/23741) — 13 comments · 12 reactions · open
- **Issue** [Upgrade Langfuse integration to Python SDK v4 and v4 OTel ingestion](https://github.com/BerriAI/litellm/issues/33383) — 6 comments · 12 reactions · open
- **Pull Request** [feat(rate-limiting): tag-scoped token/request/dollar/concurrency rate limits](https://github.com/BerriAI/litellm/pull/36541) — 67 comments · 1 reactions · open
- **Pull Request** [feat(otel/v2)!: admin-owned, identity-scoped trace destinations](https://github.com/BerriAI/litellm/pull/30873) — 52 comments · 1 reactions · open
- **Issue** [\[Bug\]: Budget enforcement bypassed in v1.82.3 for key/user max_budget despite spend exceeding max_budget](https://github.com/BerriAI/litellm/issues/26672) — 17 comments · 4 reactions · open
- **Pull Request** [feat(langfuse): upgrade SDK and OTel ingestion to v4](https://github.com/BerriAI/litellm/pull/33391) — 16 comments · 6 reactions · open
- **Pull Request** [feat(mcp): add admin-declared per-user fields for MCP servers](https://github.com/BerriAI/litellm/pull/28218) — 34 comments · 1 reactions · open
- **Pull Request** [feat(cost): support time-based off-peak pricing in cost calculation](https://github.com/BerriAI/litellm/pull/31725) — 20 comments · 3 reactions · open
- **Issue** [\[Bug\]: Lastest helm chart is pointing towards a non-existing image](https://github.com/BerriAI/litellm/issues/22173) — 6 comments · 5 reactions · open
- **Issue** [\[Feature\]: Support Azure AI Foundry Agents v2 (Responses API with agent_reference)](https://github.com/BerriAI/litellm/issues/25372) — 6 comments · 4 reactions · open
- **Issue** [\[Feature\]: Support time-based / peak-offpeak pricing for model cost calculation](https://github.com/BerriAI/litellm/issues/31606) — 2 comments · 5 reactions · open
- **Pull Request** [feat(proxy): proactive model deprecation alerts and `/model/deprecations` endpoint](https://github.com/BerriAI/litellm/pull/26900) — 26 comments · 1 reactions · closed
- **Pull Request** [feat(auto-router): scope shadow eval jobs to multiple keys](https://github.com/BerriAI/litellm/pull/36871) — 26 comments · 1 reactions · closed
- **Pull Request** [feat(complexity_router): operator-defined tier sets for the LLM classifier](https://github.com/BerriAI/litellm/pull/37226) — 27 comments · 1 reactions · closed
- **Issue** [\[Feature\]: Support salt rotating](https://github.com/BerriAI/litellm/issues/12448) — 9 comments · 3 reactions · open
- **Issue** [\[Bug\]: Setting "output_parse_pii" has no effect](https://github.com/BerriAI/litellm/issues/14516) — 11 comments · 2 reactions · closed
- **Issue** [\[Bug\]: max_end_user_budget_id ignores budget reset, leading to continuous spend accumulation](https://github.com/BerriAI/litellm/issues/24675) — 2 comments · 4 reactions · closed
- **Pull Request** [feat(triage): Agent Shin — LLM-judge + Greptile auto-close (any age, any draft state) + @agent-shin reconsider flow](https://github.com/BerriAI/litellm/pull/28117) — 22 comments · 1 reactions · open
- **Issue** [\[Bug\]: user_header_mappings does not work with OpenWebUI](https://github.com/BerriAI/litellm/issues/14667) — 12 comments · 1 reactions · closed
- **Pull Request** [fix(utils): avoid pydantic serializer warnings in validate_and_fix_openai_messages](https://github.com/BerriAI/litellm/pull/25933) — 17 comments · 2 reactions · open
- **Pull Request** [\[Fix\] Helm: honor external DB secret in standalone mode](https://github.com/BerriAI/litellm/pull/27176) — 8 comments · 4 reactions · closed
- **Pull Request** [fix(proxy): register WebSocket passthrough for OpenAI prefixes](https://github.com/BerriAI/litellm/pull/36151) — 17 comments · 1 reactions · closed
- **Issue** [\[Bug\]: litellm.llms.openai.common_utils.OpenAIError: Bad Request when using Claude Code 2.1.69](https://github.com/BerriAI/litellm/issues/22878) — 7 comments · 2 reactions · open
- **Issue** [\[Bug\]: GET /health returns extra_headers and aws_session_token in plaintext](https://github.com/BerriAI/litellm/issues/36898) — 3 comments · 2 reactions · open
- **Pull Request** [fix(oci): make Cohere {{trace}} judges work (re-land #30646, lint-clean)](https://github.com/BerriAI/litellm/pull/30780) — 18 comments · 1 reactions · open
- **Pull Request** [fix(proxy): emit sse keepalive comments during slow time-to-first-token](https://github.com/BerriAI/litellm/pull/34821) — 14 comments · 1 reactions · open
- **Pull Request** [feat(mcp): add LazyMCP gateway endpoint](https://github.com/BerriAI/litellm/pull/27754) — 12 comments · 2 reactions · closed
- **Pull Request** [fix(helm): support authenticated ServiceMonitor scrapes](https://github.com/BerriAI/litellm/pull/30565) — 17 comments · 1 reactions · open
- **Pull Request** [fix(pricing): add the azure gpt-realtime-2 family and price realtime image input per token](https://github.com/BerriAI/litellm/pull/31565) — 12 comments · 1 reactions · open

### [vLLM](https://github.com/vllm-project/vllm)

- **Issue** [\[Feature\]: Batch Invariant Feature and Performance Optimization](https://github.com/vllm-project/vllm/issues/27433) — 71 comments · 32 reactions · open
- **Issue** [\[Bug\]: MTP speculative decoding crash with illegal memory access on long sequences (Qwen3.6-27B-FP8, v0.19.1)](https://github.com/vllm-project/vllm/issues/40756) — 39 comments · 15 reactions · open
- **Issue** [\[Roadmap\] Rust Frontend Feature Parity](https://github.com/vllm-project/vllm/issues/44280) — 29 comments · 18 reactions · open
- **Pull Request** [\[Bugfix\]\[ToolParser\] Fix Qwen3 XML and Coder streaming tool call parser regressions](https://github.com/vllm-project/vllm/pull/40861) — 23 comments · 12 reactions · closed
- **Pull Request** [\[Feature\] TRITON_MLA_SPARSE backend for SM8x/11x/12x DSA Sparse MLA Support](https://github.com/vllm-project/vllm/pull/38476) — 214 comments · 11 reactions · open
- **Pull Request** [\[Core\] Extensible (growable) KV cache](https://github.com/vllm-project/vllm/pull/50779) — 26 comments · 5 reactions · open
- **Pull Request** [\[Core\]\[V1\] Support trace_decode_token_ids for deterministic decode replay](https://github.com/vllm-project/vllm/pull/46701) — 25 comments · 3 reactions · open
- **Issue** [\[Performance\]: Fully Async Spec-Decoding | Make `seq_lens_cpu` in CommonAttentionMetadata optional](https://github.com/vllm-project/vllm/issues/29134) — 7 comments · 4 reactions · open
- **Issue** [\[Bug\]: vllm/vllm-openai:latest fails to start Gemma4 with Transformers 5.15.0](https://github.com/vllm-project/vllm/issues/51744) — 15 comments · 8 reactions · open
- **Pull Request** [\[Feature\]\[Scheduler\] Add split prefix caching feature to eliminate bf16 GEMM tiling divergence across cache-hit/miss paths](https://github.com/vllm-project/vllm/pull/34046) — 27 comments · 2 reactions · open
- **Pull Request** [\[Attention\]\[Quantization\] NVFP4 KV cache on consumer/SoC Blackwell (sm120/sm121) for Gemma 3/4 via FlashInfer FA2](https://github.com/vllm-project/vllm/pull/46329) — 37 comments · 5 reactions · open
- **Pull Request** [\[Attention\]\[MLA\] FlashMLA sparse: DCP on the fp8_ds_mla mixed-batch path + MTP](https://github.com/vllm-project/vllm/pull/46514) — 55 comments · 3 reactions · open
- **Issue** [\[Perf\]\[Kernel\] Adopt PTX 9.4 `ldmatrix.s8.s4` (hardware INT4→INT8 expanding load) in W4A8-INT8 paths](https://github.com/vllm-project/vllm/issues/49529) — 15 comments · 0 reactions · open
- **Pull Request** [\[NIXL\]\[TURBOQUANT\] Support turboquant in NIXL KV connector](https://github.com/vllm-project/vllm/pull/40858) — 11 comments · 3 reactions · open
- **Pull Request** [\[Core\] Check for GPU<->CPU syncs during CI](https://github.com/vllm-project/vllm/pull/43107) — 32 comments · 3 reactions · closed
- **Pull Request** [\[Kernel\] ReplaySSM: cache SSM inputs for faster Mamba2 speculative decode](https://github.com/vllm-project/vllm/pull/49847) — 14 comments · 2 reactions · open
- **Pull Request** [\[6/N\]\[KV-Cache Layout Refactor\] Standardize KV cache layout](https://github.com/vllm-project/vllm/pull/51718) — 19 comments · 0 reactions · open
- **Issue** [\[Bug\]: Qwen3.5 CUDA Illegal Memory Access in GDN Kernel](https://github.com/vllm-project/vllm/issues/34948) — 24 comments · 2 reactions · open
- **Pull Request** [\[ROCm\]\[CI\] Gating more ROCm tests](https://github.com/vllm-project/vllm/pull/44969) — 32 comments · 2 reactions · open
- **Pull Request** [\[ModelRunner v2\] Enable MRV2 for pooling models by default](https://github.com/vllm-project/vllm/pull/48290) — 28 comments · 3 reactions · open
- **Pull Request** [\[ROCm\] DeepSeek-V4-Pro PD Disaggregation through MORI IO KV Connector on AMD GPUs](https://github.com/vllm-project/vllm/pull/48989) — 8 comments · 2 reactions · open
- **Pull Request** [\[K3\] support recoverssm for K3](https://github.com/vllm-project/vllm/pull/51855) — 8 comments · 2 reactions · closed
- **Pull Request** [\[Kernel\]\[ROCm\] Cover OCP MX MoE emulation in the mxfp4 oracle test](https://github.com/vllm-project/vllm/pull/43983) — 11 comments · 2 reactions · open
- **Pull Request** [\[Rust Frontend\] Add support for truncate_prompt_tokens and truncation_side](https://github.com/vllm-project/vllm/pull/48584) — 11 comments · 2 reactions · open
- **Pull Request** [\[kv_offload\] Session Aware Eviction Policy](https://github.com/vllm-project/vllm/pull/50422) — 6 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Fix MiniMax M3 prompt reasoning initialization](https://github.com/vllm-project/vllm/pull/50594) — 30 comments · 2 reactions · open
- **Pull Request** [Add `pydocstyle` to the `ruff` rules](https://github.com/vllm-project/vllm/pull/52136) — 7 comments · 2 reactions · open
- **Pull Request** [\[ModelRunnerV2\] Support prompt embeds](https://github.com/vllm-project/vllm/pull/42963) — 25 comments · 3 reactions · closed
- **Pull Request** [\[Bugfix\] Add Kimi K3 MoE support to benchmark_moe.py](https://github.com/vllm-project/vllm/pull/50082) — 4 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Fix speculative decoding for short_conv (LFM2) models](https://github.com/vllm-project/vllm/pull/50272) — 21 comments · 4 reactions · open

### [SGLang](https://github.com/sgl-project/sglang)

- **Issue** [\[Tracking\] CI Test Failures and Fixes](https://github.com/sgl-project/sglang/issues/17050) — 13 comments · 10 reactions · open
- **Pull Request** [\[HiCache\] Support packed and sidecar draft caches for MTP/EAGLE/DSpark](https://github.com/sgl-project/sglang/pull/30393) — 28 comments · 7 reactions · closed
- **Issue** [\[Roadmap\] Unified Hybrid Radix Cache Refactor](https://github.com/sgl-project/sglang/issues/20415) — 2 comments · 11 reactions · open
- **Pull Request** [\[HiCache\] Fix PP inconsistency with HiCache L3 (#22607)](https://github.com/sgl-project/sglang/pull/27010) — 36 comments · 3 reactions · open
- **Pull Request** [\[Model\] Support Ling-3.0-flash (BailingMoeV3)](https://github.com/sgl-project/sglang/pull/33561) — 12 comments · 9 reactions · open
- **Pull Request** [\[HiCache\] Dedup MLA KV cache in host memory across TP ranks](https://github.com/sgl-project/sglang/pull/26691) — 14 comments · 7 reactions · open
- **Pull Request** [\[FlashInfer v0.6.16\] Support FlashInfer CuTe DSL NVFP4 MoE quantization](https://github.com/sgl-project/sglang/pull/28354) — 42 comments · 0 reactions · closed
- **Pull Request** [\[DSv4\] Integrate TRT-LLM DSv4 Attention for SM100/103](https://github.com/sgl-project/sglang/pull/30805) — 59 comments · 0 reactions · open
- **Pull Request** [fix(test): stabilize nightly precision regression](https://github.com/sgl-project/sglang/pull/34668) — 38 comments · 0 reactions · open
- **Issue** [AMD Development Roadmap (2026 Q3)](https://github.com/sgl-project/sglang/issues/35003) — 0 comments · 6 reactions · open
- **Pull Request** [\[AMD\] Add fused all-reduce RMSNorm per-token FP8/MXFP4 quant](https://github.com/sgl-project/sglang/pull/29723) — 16 comments · 2 reactions · open
- **Pull Request** [\[Diffusion\] Reuse SRT SigLIP in Pi0.5](https://github.com/sgl-project/sglang/pull/34992) — 0 comments · 0 reactions · closed
- **Issue** [\[Feature\] RFC: SGLang KV Indexer for Distributed KV Cache Placement Metadata](https://github.com/sgl-project/sglang/issues/31458) — 2 comments · 4 reactions · open
- **Pull Request** [\[AMD\] Enable gfx1250 Support](https://github.com/sgl-project/sglang/pull/32754) — 19 comments · 1 reactions · open
- **Pull Request** [feat: Add DeepSeek V4 SWA recompute](https://github.com/sgl-project/sglang/pull/31713) — 0 comments · 6 reactions · open
- **Pull Request** [\[NPU\] \[Diffusion\] Support MiniMax H3 on Ascend NPU's](https://github.com/sgl-project/sglang/pull/33569) — 20 comments · 0 reactions · open
- **Pull Request** [TP/PP Consensus checker](https://github.com/sgl-project/sglang/pull/34406) — 1 comments · 5 reactions · open
- **Issue** [\[Bug\] GLM-5.2-NVFP4 error on pro6000](https://github.com/sgl-project/sglang/issues/29562) — 15 comments · 0 reactions · open
- **Pull Request** [feat(diffusion): add OmniDreams autoregressive video world model](https://github.com/sgl-project/sglang/pull/27442) — 15 comments · 1 reactions · open
- **Pull Request** [\[AMD\] \[GLM5\] fp8 MLA absorbed bmm for GLM-5.2 on gfx950](https://github.com/sgl-project/sglang/pull/30519) — 10 comments · 2 reactions · closed
- **Pull Request** [\[Spec\] Fix Dspark and Dflash state divergence across TP rank](https://github.com/sgl-project/sglang/pull/33614) — 15 comments · 1 reactions · open
- **Pull Request** [Profiling Enhancements \[2/3\]: detailed execution step annotations](https://github.com/sgl-project/sglang/pull/24911) — 12 comments · 1 reactions · open
- **Pull Request** [\[DSA\] Skip indexer KV cache for skip-topk layers](https://github.com/sgl-project/sglang/pull/30531) — 16 comments · 0 reactions · closed
- **Pull Request** [\[AMD\] Optimize KIMI-K3 with Triton MLA decode kernel by tuning the stage-1 geometry for gfx950](https://github.com/sgl-project/sglang/pull/34580) — 9 comments · 2 reactions · open
- **Issue** [\[Bug\] DeepSeek-V4 sparse attention indexer (`fp8_paged_mqa_logits`) illegal memory access with long-context requests](https://github.com/sgl-project/sglang/issues/34718) — 2 comments · 1 reactions · open
- **Pull Request** [\[FlashInfer v0.6.13\] Use CuTe DSL backend for FlashInfer per-token NVFP4 quantization](https://github.com/sgl-project/sglang/pull/28220) — 15 comments · 1 reactions · closed
- **Pull Request** [\[PD\] Introduce runtime role switching between prefill and decode](https://github.com/sgl-project/sglang/pull/28403) — 7 comments · 3 reactions · open
- **Pull Request** [\[3/N\] elastic-ep: Recapture decode CUDA graphs after scale-up](https://github.com/sgl-project/sglang/pull/33723) — 18 comments · 0 reactions · open
- **Pull Request** [fix(bcg): preserve Qwen3-VL DeepStack inputs during replay](https://github.com/sgl-project/sglang/pull/33726) — 14 comments · 0 reactions · open
- **Pull Request** [bugfix: prevent excessive token slot reservation](https://github.com/sgl-project/sglang/pull/16807) — 16 comments · 0 reactions · closed

### [Ray](https://github.com/ray-project/ray)

- **Issue** [\[serve\]\[llm\] Governance middleware layer for Ray Serve LLM — PII detection, cost budgets, policy enforcement, and audit trails](https://github.com/ray-project/ray/issues/65259) — 10 comments · 0 reactions · open
- **Issue** [\[core\]\[rdt\] Make memory pool copies async](https://github.com/ray-project/ray/issues/65399) — 1 comments · 0 reactions · open
- **Issue** [\[GCS\] Use Redis UNLINK instead of DEL when cleaning a persisted namespace](https://github.com/ray-project/ray/issues/65520) — 0 comments · 0 reactions · open
- **Issue** [\[Data\] Add `max_concurrent_calls_per_actor` to ActorPoolStrategy](https://github.com/ray-project/ray/issues/65529) — 0 comments · 0 reactions · open
- **Issue** [\[data\] A fast upstream actor pool can starve a slow-starting downstream bottleneck](https://github.com/ray-project/ray/issues/65540) — 0 comments · 0 reactions · open
- **Issue** [\[Data\] map_batches/iter_batches streaming read holds 2-5x the dataset's uncompressed size as RSS, invisible to Ray's own object-store/task accounting](https://github.com/ray-project/ray/issues/65544) — 0 comments · 0 reactions · open
- **Pull Request** [\[Core\] Fix Windows fatal access violation during ActorPool teardown with runtime_env (Fixes #62442)](https://github.com/ray-project/ray/pull/63992) — 18 comments · 2 reactions · open
- **Pull Request** [Bump js-yaml from 4.1.0 to 4.3.0 in /python/ray/dashboard/client](https://github.com/ray-project/ray/pull/64888) — 1 comments · 0 reactions · open
- **Issue** [\[Core\] Core gentle walkthrough example doesn't show the benefit of Ray.](https://github.com/ray-project/ray/issues/40653) — 7 comments · 0 reactions · open
- **Issue** [\[core\] Unify executor threads when enabling/disabling concurrency_groups](https://github.com/ray-project/ray/issues/54639) — 4 comments · 0 reactions · open
- **Pull Request** [\[data\] Add orc datasource for V2](https://github.com/ray-project/ray/pull/64540) — 7 comments · 1 reactions · open
- **Pull Request** [\[dashboard\] Configurable defaults + UI dialogs for py-spy/memray profiling params](https://github.com/ray-project/ray/pull/64806) — 7 comments · 1 reactions · open
- **Pull Request** [\[core\] Enable TCP keepalive on GCS<->Redis connections](https://github.com/ray-project/ray/pull/65424) — 2 comments · 2 reactions · open
- **Pull Request** [\[docs\] add initial documentation for Ray sandboxing](https://github.com/ray-project/ray/pull/65503) — 2 comments · 2 reactions · closed
- **Issue** [\[Core\] Randomize worker port allocation to reduce deterministic collisions between raylets](https://github.com/ray-project/ray/issues/65444) — 0 comments · 0 reactions · open
- **Issue** [\[core\]\[scheduler\] Iterator invalidation in node label scheduling filter](https://github.com/ray-project/ray/issues/65517) — 1 comments · 0 reactions · open
- **Pull Request** [\[Data\] Add checkpoint support for Iceberg read/write](https://github.com/ray-project/ray/pull/61753) — 9 comments · 1 reactions · open
- **Pull Request** [\[Data\] Disallow min_rows_per_file with partitioned parquet writes](https://github.com/ray-project/ray/pull/63368) — 5 comments · 1 reactions · open
- **Pull Request** [\[core\]\[joblib\] Add opt-in autoscaling to ray.util.multiprocessing.Pool](https://github.com/ray-project/ray/pull/64957) — 9 comments · 1 reactions · open
- **Pull Request** [\[core\]\[dashboard\] Return 4xx from node and actor detail APIs](https://github.com/ray-project/ray/pull/65015) — 4 comments · 1 reactions · open
- **Pull Request** [Fix/tls server cert hot reload](https://github.com/ray-project/ray/pull/65390) — 4 comments · 1 reactions · open
- **Pull Request** [fix(autoscaler): deduplicate cloud instances during termination](https://github.com/ray-project/ray/pull/65419) — 0 comments · 2 reactions · open
- **Pull Request** [\[train\] Share PlacementGroupCleaner across Train runs](https://github.com/ray-project/ray/pull/65447) — 0 comments · 2 reactions · open
- **Issue** [\[data\] ds.summary() crashes on boolean columns with ArrowNotImplementedError](https://github.com/ray-project/ray/issues/62235) — 3 comments · 0 reactions · open
- **Pull Request** [\[Data\] Fix ResourceBudget backpressure causing pipeline stall](https://github.com/ray-project/ray/pull/64601) — 3 comments · 1 reactions · open
- **Pull Request** [\[Autoscaler\]\[AWS\] Retry key pair creation after duplicate](https://github.com/ray-project/ray/pull/64738) — 2 comments · 1 reactions · open
- **Pull Request** [\[Feat\]\[Core/Auth\] Enable token authentication for local clusters by default](https://github.com/ray-project/ray/pull/64755) — 2 comments · 1 reactions · open
- **Pull Request** [\[serve\] Deflake test_metrics suites on constrained CI runners](https://github.com/ray-project/ray/pull/64876) — 6 comments · 1 reactions · closed
- **Pull Request** [\[Data\] Fix LeRobot delta windows for multidimensional features](https://github.com/ray-project/ray/pull/65165) — 2 comments · 2 reactions · closed
- **Pull Request** [refactor(setup): modernize string formatting and ensure explicit file encoding](https://github.com/ray-project/ray/pull/65439) — 2 comments · 1 reactions · open

### [BentoML](https://github.com/bentoml/BentoML)

- **Pull Request** [feat: agent skills for deploying BentoML services to Kubernetes and EC2](https://github.com/bentoml/BentoML/pull/5683) — 0 comments · 0 reactions · open
- **Pull Request** [fix: Windows tar symlink extraction and fastai CI dependency resolution](https://github.com/bentoml/BentoML/pull/5689) — 0 comments · 0 reactions · open
