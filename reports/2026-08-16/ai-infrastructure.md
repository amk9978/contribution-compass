# AI Infrastructure — 2026-08-16

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [\[Feature\]: Tracking Whisper feature requests](https://github.com/vllm-project/vllm/issues/25750)

- Project: `vllm-project/vllm`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: help wanted, good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[Feature\]: Composite model loading using `AutoWeightsLoader` for all models](https://github.com/vllm-project/vllm/issues/15697)

- Project: `vllm-project/vllm`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[Perf\]\[Kernel\] Adopt PTX 9.4 `ldmatrix.s8.s4` (hardware INT4→INT8 expanding load) in W4A8-INT8 paths](https://github.com/vllm-project/vllm/issues/49529)

- Project: `vllm-project/vllm`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[Bug\]: chatgpt/gpt-5.4 returns empty final Responses output, and completion() bridge fails with "Unknown items in responses API response: \[\]"](https://github.com/BerriAI/litellm/issues/25429)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Qwen/Qwen3.5-27B Batch Inference very slow / not working](https://github.com/vllm-project/vllm/issues/36010)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [LiteLLM](https://github.com/BerriAI/litellm)

- **Issue** [\[Feature\]: Dark Mode](https://github.com/BerriAI/litellm/issues/10177) — 63 comments · 84 reactions · open
- **Issue** [\[Bug\]: chatgpt/gpt-5.4 returns empty final Responses output, and completion() bridge fails with "Unknown items in responses API response: \[\]"](https://github.com/BerriAI/litellm/issues/25429) — 18 comments · 4 reactions · open
- **Pull Request** [Allow LLM API keys to access model info endpoints](https://github.com/BerriAI/litellm/pull/20766) — 9 comments · 7 reactions · open
- **Issue** [\[Feature\]: LiteLLM Operator for deeper integration with Kubernetes and GitOps.](https://github.com/BerriAI/litellm/issues/18428) — 5 comments · 5 reactions · open
- **Pull Request** [feat(auto-router): scope shadow eval jobs to multiple keys](https://github.com/BerriAI/litellm/pull/36871) — 25 comments · 1 reactions · open
- **Issue** [Helm Chart: Switch to other repo provider for postgres and redis dependencies](https://github.com/BerriAI/litellm/issues/19769) — 6 comments · 4 reactions · open
- **Pull Request** [feat(proxy): proactive model deprecation alerts and `/model/deprecations` endpoint](https://github.com/BerriAI/litellm/pull/26900) — 22 comments · 1 reactions · open
- **Pull Request** [feat(cost): support time-based off-peak pricing in cost calculation](https://github.com/BerriAI/litellm/pull/31725) — 19 comments · 2 reactions · open
- **Pull Request** [feat: shadow eval samples /v1/messages and /v1/responses traffic](https://github.com/BerriAI/litellm/pull/36830) — 22 comments · 1 reactions · closed
- **Pull Request** [fix(cost): tiered pricing supports cache creation cost and is all-or-nothing](https://github.com/BerriAI/litellm/pull/36720) — 20 comments · 1 reactions · closed
- **Pull Request** [feat(vertex_ai): add Lyria music generation support](https://github.com/BerriAI/litellm/pull/30304) — 23 comments · 1 reactions · open
- **Pull Request** [fix(streaming): backfill response.completed output from output_item.done events](https://github.com/BerriAI/litellm/pull/31332) — 15 comments · 2 reactions · open
- **Pull Request** [fix(anthropic): populate inference_geo from the request so regional pricing applies](https://github.com/BerriAI/litellm/pull/34857) — 12 comments · 1 reactions · closed
- **Pull Request** [feat(mcp): scope gateway session bearers to the RFC 8707 resource](https://github.com/BerriAI/litellm/pull/35045) — 13 comments · 1 reactions · closed
- **Pull Request** [fix(vertex_ai): translate /v1/embeddings batch rows to the Gemini embedding shape](https://github.com/BerriAI/litellm/pull/35092) — 13 comments · 1 reactions · closed
- **Pull Request** [fix(bedrock): register managed-batch litellm_params so they stop leaking to the provider](https://github.com/BerriAI/litellm/pull/36633) — 13 comments · 1 reactions · closed
- **Pull Request** [fix(proxy): requeue spend logs when the DB write fails with a transport error](https://github.com/BerriAI/litellm/pull/36716) — 13 comments · 1 reactions · closed
- **Pull Request** [feat(bedrock): forward LiteLLM identity and metadata into Bedrock requestMetadata](https://github.com/BerriAI/litellm/pull/36861) — 13 comments · 1 reactions · open
- **Pull Request** [fix(guardrails): return the full PANW AIRS scan response on blocked requests](https://github.com/BerriAI/litellm/pull/37036) — 16 comments · 1 reactions · closed
- **Pull Request** [fix(panw_prisma_airs): scan tool call args as plain text, not a tool_event](https://github.com/BerriAI/litellm/pull/37038) — 17 comments · 1 reactions · closed
- **Pull Request** [fix(ui): show key edit for team members granted /key/update](https://github.com/BerriAI/litellm/pull/31958) — 14 comments · 1 reactions · open
- **Pull Request** [feat(azure): add support for apply_guardrail within Azure guardrails](https://github.com/BerriAI/litellm/pull/35990) — 11 comments · 1 reactions · open
- **Pull Request** [fix(streaming): preserve prompt cache usage details](https://github.com/BerriAI/litellm/pull/36089) — 10 comments · 1 reactions · open
- **Pull Request** [fix(proxy): accept virtual keys on include_subpath pass-through sub-paths](https://github.com/BerriAI/litellm/pull/36389) — 10 comments · 1 reactions · open
- **Pull Request** [fix(UI): add default model pin to complexity router UI](https://github.com/BerriAI/litellm/pull/36615) — 11 comments · 1 reactions · open
- **Pull Request** [feat(langfuse): migrate the sdk callback to langfuse v4](https://github.com/BerriAI/litellm/pull/36741) — 10 comments · 1 reactions · open
- **Pull Request** [fix(langfuse)!: source the emitted metadata blob from StandardLoggingPayload](https://github.com/BerriAI/litellm/pull/36744) — 10 comments · 1 reactions · closed
- **Pull Request** [feat(lint): exempt TypedDict-annotated dict literals from LIT002](https://github.com/BerriAI/litellm/pull/36813) — 10 comments · 1 reactions · closed
- **Pull Request** [fix(batches): account a managed batch's cost exactly once](https://github.com/BerriAI/litellm/pull/36877) — 11 comments · 1 reactions · closed
- **Pull Request** [feat: add TealTiger as a custom guardrail plugin](https://github.com/BerriAI/litellm/pull/36912) — 10 comments · 1 reactions · open

### [vLLM](https://github.com/vllm-project/vllm)

- **Issue** [\[Feature\]: Tracking Whisper feature requests](https://github.com/vllm-project/vllm/issues/25750) — 18 comments · 17 reactions · open
- **Pull Request** [\[Kernel\] adding native nccl4py support](https://github.com/vllm-project/vllm/pull/33127) — 35 comments · 4 reactions · open
- **Pull Request** [\[DO NOT MERGE\]\[Perf\]\[DSv4\] Add generic cuteDSL LL Blockwise FP8 GEMM with PDL](https://github.com/vllm-project/vllm/pull/43214) — 11 comments · 4 reactions · open
- **Issue** [\[Feature\]: Composite model loading using `AutoWeightsLoader` for all models](https://github.com/vllm-project/vllm/issues/15697) — 44 comments · 0 reactions · open
- **Issue** [\[Feature\]: Support qwen3next with GGUF?](https://github.com/vllm-project/vllm/issues/30023) — 6 comments · 8 reactions · closed
- **Issue** [\[Perf\]\[Kernel\] Adopt PTX 9.4 `ldmatrix.s8.s4` (hardware INT4→INT8 expanding load) in W4A8-INT8 paths](https://github.com/vllm-project/vllm/issues/49529) — 14 comments · 0 reactions · open
- **Pull Request** [\[NIXL\]\[TURBOQUANT\] Support turboquant in NIXL KV connector](https://github.com/vllm-project/vllm/pull/40858) — 11 comments · 3 reactions · open
- **Issue** [\[Bug\]: Qwen3-VL-30B-A3B-Instruct keeps outputting the same phrases over and over](https://github.com/vllm-project/vllm/issues/27157) — 16 comments · 5 reactions · open
- **Issue** [\[Bug\]: Performance Bottlenecks and V1 Engine Instability on AMD gfx1151 (Strix Halo)](https://github.com/vllm-project/vllm/issues/32180) — 8 comments · 1 reactions · open
- **Pull Request** [\[Bugfix\] Sync xgrammar termination state after failed token acceptance](https://github.com/vllm-project/vllm/pull/37506) — 7 comments · 9 reactions · open
- **Pull Request** [\[K3\] support recoverssm for K3](https://github.com/vllm-project/vllm/pull/51855) — 4 comments · 2 reactions · open
- **Pull Request** [\[ROCm\]\[DSV4\]\[Perf\] Optimize Triton sparse-MLA decode on gfx950](https://github.com/vllm-project/vllm/pull/52212) — 5 comments · 2 reactions · open
- **Issue** [\[Feature\]: Unwrap FusedMoE custom op](https://github.com/vllm-project/vllm/issues/31985) — 27 comments · 1 reactions · open
- **Pull Request** [\[Frontend\] Add FP8 output quantization support to FlashAttention backend](https://github.com/vllm-project/vllm/pull/31636) — 38 comments · 0 reactions · open
- **Pull Request** [\[ModelRunner V2\] Speculative Decoding NGram GPU Implementations](https://github.com/vllm-project/vllm/pull/40704) — 22 comments · 3 reactions · open
- **Pull Request** [\[ModelRunner v2\] Enable MRV2 for pooling models by default](https://github.com/vllm-project/vllm/pull/48290) — 23 comments · 3 reactions · open
- **Pull Request** [\[Bugfix\] Fix MiniMax M3 prompt reasoning initialization](https://github.com/vllm-project/vllm/pull/50594) — 27 comments · 2 reactions · open
- **Pull Request** [\[ModelRunnerV2\] Support prompt embeds](https://github.com/vllm-project/vllm/pull/42963) — 20 comments · 3 reactions · open
- **Pull Request** [\[Kernel\]\[Kimi\] fused vision q/k roper kernel](https://github.com/vllm-project/vllm/pull/50400) — 5 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Make DSV4 sparse MLA work end-to-end for plain decode, MTP, and DSpark](https://github.com/vllm-project/vllm/pull/51538) — 25 comments · 2 reactions · closed
- **Pull Request** [fix(v1): decouple async Mamba align D2H counts from InputBatch row shifts (#51571)](https://github.com/vllm-project/vllm/pull/51599) — 24 comments · 2 reactions · open
- **Pull Request** [\[Core\] Add per-request prefix-cache write policy](https://github.com/vllm-project/vllm/pull/51981) — 1 comments · 2 reactions · open
- **Pull Request** [Enable return_routed_experts support with CPU KV offload](https://github.com/vllm-project/vllm/pull/45635) — 22 comments · 3 reactions · open
- **Pull Request** [\[Frontend\] Enforce max_tool_calls for Responses built-in tools](https://github.com/vllm-project/vllm/pull/47112) — 2 comments · 2 reactions · open
- **Pull Request** [\[Offloader\] Prefetch weight offloading for large MoE models, plus a schedule planner](https://github.com/vllm-project/vllm/pull/51710) — 2 comments · 2 reactions · open
- **Issue** [\[Responses API\] Support tool calling and ouput token streaming](https://github.com/vllm-project/vllm/issues/27263) — 12 comments · 3 reactions · closed
- **Issue** [\[RFC\]: Support function calling using `structural_tag`.](https://github.com/vllm-project/vllm/issues/32142) — 4 comments · 5 reactions · closed
- **Pull Request** [\[Kimi-K3\]\[AMD\] Return KDA and MLA projection outputs directly](https://github.com/vllm-project/vllm/pull/50592) — 20 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\]\[Kernel\] Fix divergent warp collectives in partial NeoX QK-Norm+RoPE](https://github.com/vllm-project/vllm/pull/50903) — 21 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Temporarily disable FA4 head-dim 256](https://github.com/vllm-project/vllm/pull/52050) — 21 comments · 2 reactions · open

### [SGLang](https://github.com/sgl-project/sglang)

- **Issue** [\[Tracking\] CI Test Failures and Fixes](https://github.com/sgl-project/sglang/issues/17050) — 13 comments · 10 reactions · open
- **Issue** [\[Roadmap\] Unified Hybrid Radix Cache Refactor](https://github.com/sgl-project/sglang/issues/20415) — 2 comments · 11 reactions · open
- **Issue** [\[Feature\] Improve Unit Test Coverage](https://github.com/sgl-project/sglang/issues/20865) — 85 comments · 0 reactions · open
- **Issue** [\[Feature\] Load Balance Refactor for DP-Attention](https://github.com/sgl-project/sglang/issues/16080) — 8 comments · 7 reactions · closed
- **Pull Request** [\[DSv4\] Integrate TRT-LLM DSv4 Attention for SM100/103](https://github.com/sgl-project/sglang/pull/30805) — 44 comments · 0 reactions · open
- **Pull Request** [\[PP&Spec\] enable speculative decoding (eagle_worker_v2) under PP](https://github.com/sgl-project/sglang/pull/31139) — 22 comments · 4 reactions · open
- **Pull Request** [\[AMD\]\[Quantization\] Online MXFP4 quantization 4/N - NVFP4 to MXFP4 Online Requantization on AMD GPUs](https://github.com/sgl-project/sglang/pull/29328) — 24 comments · 1 reactions · closed
- **Pull Request** [fix(test): stabilize nightly precision regression](https://github.com/sgl-project/sglang/pull/34668) — 26 comments · 0 reactions · open
- **Pull Request** [\[AMD\] Enable gfx1250 Support](https://github.com/sgl-project/sglang/pull/32754) — 16 comments · 1 reactions · open
- **Issue** [\[Help\] \[Performance\] PD disaggregation on H200 shows no throughput gain over single-node traditional deployment with 32k input / 512 output](https://github.com/sgl-project/sglang/issues/24488) — 3 comments · 3 reactions · open
- **Pull Request** [\[AMD\] \[GLM5\] Enable dense-MHA short-context prefill fallback on gfx950](https://github.com/sgl-project/sglang/pull/30808) — 19 comments · 0 reactions · closed
- **Pull Request** [\[XPU\]\[Diffusion\] Enable MiniMax H3 on XPU platforms](https://github.com/sgl-project/sglang/pull/33366) — 18 comments · 0 reactions · open
- **Issue** [\[Bug\] \[Diffusion\] Attention backend fallback change introduced errors on most models](https://github.com/sgl-project/sglang/issues/34389) — 9 comments · 0 reactions · closed
- **Pull Request** [\[NPU\] Add mxfp4-w4a8 MOE Quantization Support for NPU](https://github.com/sgl-project/sglang/pull/30318) — 17 comments · 0 reactions · open
- **Pull Request** [\[DSA\] Skip indexer KV cache for skip-topk layers](https://github.com/sgl-project/sglang/pull/30531) — 16 comments · 0 reactions · open
- **Pull Request** [\[NPU\] \[Diffusion\] Support MiniMax H3 on Ascend NPU's](https://github.com/sgl-project/sglang/pull/33569) — 16 comments · 0 reactions · open
- **Pull Request** [Profiling Enhancements \[2/3\]: detailed execution step annotations](https://github.com/sgl-project/sglang/pull/24911) — 10 comments · 1 reactions · open
- **Pull Request** [\[AMD\] Optimize KIMI-K3 with Triton MLA decode kernel by tuning the stage-1 geometry for gfx950](https://github.com/sgl-project/sglang/pull/34580) — 6 comments · 2 reactions · open
- **Pull Request** [fix(bcg): preserve Qwen3-VL DeepStack inputs during replay](https://github.com/sgl-project/sglang/pull/33726) — 13 comments · 0 reactions · open
- **Pull Request** [\[bugfix\] fix for qwen2-vl quant](https://github.com/sgl-project/sglang/pull/14682) — 11 comments · 1 reactions · closed
- **Pull Request** [\[AMD\] Enable Fast Triton Sparse MLA backend](https://github.com/sgl-project/sglang/pull/30575) — 7 comments · 1 reactions · open
- **Issue** [HiCache: HiMambaRadixCache crashes with 'Destination indices must be a CUDA tensor' on Qwen3.5/3.6](https://github.com/sgl-project/sglang/issues/24121) — 4 comments · 0 reactions · closed
- **Issue** [\[Feature\] dLLM performance optimization in prefill and batching](https://github.com/sgl-project/sglang/issues/24644) — 4 comments · 0 reactions · closed
- **Issue** [gRPC mode: --enable-metrics error message cites wrong servicer version (≥0.5.3 → should be ≥0.5.5); v0.5.13 image ships 0.5.4 and fails to boot](https://github.com/sgl-project/sglang/issues/28298) — 4 comments · 0 reactions · closed
- **Issue** [\[Bug\] Kimi-K3 tool call parser fails ~8x/hour in production: TypeError 'string indices must be integers' and json 'unexpected character'](https://github.com/sgl-project/sglang/issues/34604) — 0 comments · 0 reactions · open
- **Issue** [\[Bug\] Scheduler crashes with AttributeError ('list' object has no attribute 'tolist') on mixed batches with token_ids_logprob — prefill and decode paths, v0.5.14–v0.5.17](https://github.com/sgl-project/sglang/issues/34719) — 1 comments · 0 reactions · open
- **Pull Request** [\[Kernel\] Enable Helion backend for Kimi Delta-Attention](https://github.com/sgl-project/sglang/pull/32593) — 9 comments · 0 reactions · closed
- **Pull Request** [\[AMD\]\[Spec\] Accelerate Qwen3.5 verification with grouped-head shared KV](https://github.com/sgl-project/sglang/pull/34517) — 4 comments · 1 reactions · closed
- **Pull Request** [\[Diffusion\] Unify component residency controls](https://github.com/sgl-project/sglang/pull/34736) — 8 comments · 0 reactions · open
- **Pull Request** [Fix swa eviction frontier for bigram keys](https://github.com/sgl-project/sglang/pull/34870) — 8 comments · 0 reactions · open

### [Ray](https://github.com/ray-project/ray)

- **Issue** [\[Core\] Core gentle walkthrough example doesn't show the benefit of Ray.](https://github.com/ray-project/ray/issues/40653) — 6 comments · 0 reactions · open
- **Pull Request** [\[Data\]\[1/N\] add external shuffle runtime library](https://github.com/ray-project/ray/pull/64828) — 4 comments · 1 reactions · closed
- **Pull Request** [\[Data\] Disallow min_rows_per_file with partitioned parquet writes](https://github.com/ray-project/ray/pull/63368) — 3 comments · 1 reactions · open
- **Pull Request** [\[dashboard\] Configurable defaults + UI dialogs for py-spy/memray profiling params](https://github.com/ray-project/ray/pull/64806) — 7 comments · 1 reactions · open
- **Pull Request** [\[Data\]\[LLM\] Add multi-host TPU batch inference for Ray Data LLM](https://github.com/ray-project/ray/pull/65422) — 3 comments · 1 reactions · open
- **Pull Request** [refactor(setup): modernize string formatting and ensure explicit file encoding](https://github.com/ray-project/ray/pull/65439) — 2 comments · 1 reactions · open
- **Pull Request** [\[Data\] Add support for writing ORC files](https://github.com/ray-project/ray/pull/65453) — 3 comments · 1 reactions · open
- **Issue** [\[Data\] Add named remote parameters to read APIs](https://github.com/ray-project/ray/issues/65500) — 0 comments · 0 reactions · open
- **Issue** [\[Data\] Remove existing chaos and autoscaling release test variants](https://github.com/ray-project/ray/issues/65504) — 0 comments · 0 reactions · open
- **Pull Request** [\[Serve\] \[SGLang\] \[POC\]  PD disaggregation](https://github.com/ray-project/ray/pull/63741) — 5 comments · 1 reactions · open
- **Pull Request** [\[Data\] \[5/11\] Add the Parquet FooterReader actor pool](https://github.com/ray-project/ray/pull/65273) — 1 comments · 1 reactions · open
- **Pull Request** [\[Data\] Update docs for hash shuffle v2](https://github.com/ray-project/ray/pull/65372) — 1 comments · 1 reactions · closed
- **Pull Request** [\[Data\] OpTask._cancel never passes force=True](https://github.com/ray-project/ray/pull/65389) — 0 comments · 1 reactions · open
- **Pull Request** [\[doc\]\[History server\] Update doc for history server for `RAY_ROOT_DIR` -> `STORAGE_ROOT_DIR`](https://github.com/ray-project/ray/pull/65441) — 1 comments · 1 reactions · closed
- **Pull Request** [\[docs\] Lowercase "Ray dashboard" across the docs](https://github.com/ray-project/ray/pull/65468) — 0 comments · 1 reactions · open
- **Pull Request** [\[Data\] Pin fused map function for shuffle tasks](https://github.com/ray-project/ray/pull/65480) — 0 comments · 1 reactions · open
- **Pull Request** [\[Serve\] Add enable_strict_max_ongoing_requests deployment flag](https://github.com/ray-project/ray/pull/65497) — 0 comments · 1 reactions · open
- **Pull Request** [\[Docs\]\[KubeRay\] Use RayJob sample YAML for History Server docs](https://github.com/ray-project/ray/pull/65505) — 0 comments · 2 reactions · open
- **Pull Request** [\[core\]\[metrics\] Add PrometheusCollector: mirror any /metrics exposition into Ray metrics](https://github.com/ray-project/ray/pull/64671) — 3 comments · 1 reactions · closed
- **Pull Request** [\[core\] Removing unused constants from constants.h](https://github.com/ray-project/ray/pull/64792) — 2 comments · 1 reactions · closed
- **Pull Request** [\[Data\]\[2/N\] add external shuffle task+operators](https://github.com/ray-project/ray/pull/65144) — 0 comments · 1 reactions · open
- **Pull Request** [\[core\] Export the cluster ID to node-spawned processes instead of fetching it from the GCS](https://github.com/ray-project/ray/pull/65156) — 1 comments · 1 reactions · open
- **Pull Request** [\[Core\] Free unconsumed object reported for deleted generator](https://github.com/ray-project/ray/pull/65276) — 0 comments · 1 reactions · open
- **Pull Request** [\[Docs\]\[KubeRay\] Update all KubeRay version references to 1.7.0](https://github.com/ray-project/ray/pull/65498) — 1 comments · 1 reactions · open
- **Pull Request** [\[Data\]\[3/n\] external shuffle planner](https://github.com/ray-project/ray/pull/65499) — 0 comments · 1 reactions · open
- **Pull Request** [\[Data\] Deprecate ray_remote_args for read APIs](https://github.com/ray-project/ray/pull/65501) — 0 comments · 1 reactions · open
- **Pull Request** [feat: get draining nodes in Ray Serve controller](https://github.com/ray-project/ray/pull/65502) — 0 comments · 1 reactions · open
- **Pull Request** [add initial documentation for Ray sandboxing](https://github.com/ray-project/ray/pull/65503) — 0 comments · 1 reactions · open
- **Pull Request** [\[air\](deps): Bump torch from 2.9.0 to 2.12.1+cpu in /python/requirements/ml](https://github.com/ray-project/ray/pull/64859) — 3 comments · 0 reactions · closed

### [BentoML](https://github.com/bentoml/BentoML)

- **Issue** [bug: Async Return Latency Issues with BentoML Image IO API](https://github.com/bentoml/BentoML/issues/4863) — 1 comments · 0 reactions · open
- **Pull Request** [fix: sanitize newlines in docker env dict values and v2 env rendering](https://github.com/bentoml/BentoML/pull/5692) — 2 comments · 0 reactions · open
- **Pull Request** [fix: send one multipart part per URL in list file fields](https://github.com/bentoml/BentoML/pull/5691) — 1 comments · 0 reactions · open
