# AI Infrastructure — 2026-08-21

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [\[Data\] write_lance is incompatible with PyLance 6.x due to removed storage_options_provider argument](https://github.com/ray-project/ray/issues/65129)

- Project: `ray-project/ray`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[Feature\]: Enable LoRA support for tower and connector in more MM models](https://github.com/vllm-project/vllm/issues/31479)

- Project: `vllm-project/vllm`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: help wanted; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [\[Bug\]: Latest Nightly build with TurboQuant KV cache crashes on large chunked continuation prefill after workspace lock ( testing PR #39931 implementing TQ on Hybrid Attention Models e.g Qwen3.5-9B)](https://github.com/vllm-project/vllm/issues/41726)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Core\] - providing `py_executable=uv run` causes failures with unloadable logs](https://github.com/ray-project/ray/issues/54275)

- Project: `ray-project/ray`
- Tier: `triage-lead`
- Evidence: Documentation-related issue with no assignee listed
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Gemini models degenerate in multi-turn tool-calling via /v1/messages — thoughtSignature not propagated from thought parts](https://github.com/BerriAI/litellm/issues/25322)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Based on Qwen3.5-35B-A3B, why does enabling MTP speculative decoding actually reduce the prefix cache hit rate?](https://github.com/vllm-project/vllm/issues/38182)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug/Docs\]: Snowflake (snowflake/) provider: streaming tool-calls dropped, misleading endpoint docs, and gaps using the OpenAI-/Anthropic-compatible Cortex endpoints](https://github.com/BerriAI/litellm/issues/30762)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Unexpected log messages about unresolved cost information with Docker image 1.90.0](https://github.com/BerriAI/litellm/issues/32484)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [Ray logging function not quite working](https://github.com/ray-project/ray/issues/46644)

- Project: `ray-project/ray`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [\[Bug\]: Qwen3.6-27B (dense Gated-DeltaNet) permanently hard-wedges the V1 engine — two reproducible modes (2 large images; long multi-turn text), possibly related](https://github.com/vllm-project/vllm/issues/52551)

- Project: `vllm-project/vllm`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [LiteLLM](https://github.com/BerriAI/litellm)

- **Issue** [\[Bug\]: issue while adding Custom MCP server](https://github.com/BerriAI/litellm/issues/23869) — 17 comments · 9 reactions · closed
- **Pull Request** [feat(guardrails): add Lakera v2 skip-message honoring and advisory (inject_system_message) mode](https://github.com/BerriAI/litellm/pull/34940) — 45 comments · 1 reactions · open
- **Pull Request** [feat(rate-limiting): tag-scoped token/request/dollar/concurrency rate limits](https://github.com/BerriAI/litellm/pull/36541) — 130 comments · 1 reactions · open
- **Pull Request** [feat(ui): add and delete auto-router tiers with classifier definitions](https://github.com/BerriAI/litellm/pull/37246) — 61 comments · 1 reactions · open
- **Pull Request** [feat(ui): multi-key shadow eval picker and per-key breakdown](https://github.com/BerriAI/litellm/pull/37389) — 42 comments · 1 reactions · closed
- **Pull Request** [feat(rust): route /chat/completions through the Rust core for anthropic and bedrock](https://github.com/BerriAI/litellm/pull/37241) — 38 comments · 1 reactions · closed
- **Pull Request** [feat(shadow_eval)!: gate the per-key budget on dollar spend instead of turns](https://github.com/BerriAI/litellm/pull/37555) — 36 comments · 1 reactions · closed
- **Issue** [\[Bug\]: Provider List: https://docs.litellm.ai/docs/providers](https://github.com/BerriAI/litellm/issues/23879) — 6 comments · 6 reactions · closed
- **Pull Request** [fix: omit thinking.type=disabled for always-on thinking Claude models](https://github.com/BerriAI/litellm/pull/37510) — 34 comments · 1 reactions · open
- **Pull Request** [feat(cli): store the lite login credential in the OS keychain](https://github.com/BerriAI/litellm/pull/37566) — 32 comments · 1 reactions · closed
- **Issue** [\[Bug\]: DB exception in update_spend job](https://github.com/BerriAI/litellm/issues/15519) — 6 comments · 6 reactions · open
- **Pull Request** [feat(proxy): redact or drop individual batch records instead of rejecting the file](https://github.com/BerriAI/litellm/pull/37561) — 31 comments · 1 reactions · closed
- **Pull Request** [fix(streaming): backfill response.completed output from output_item.done events](https://github.com/BerriAI/litellm/pull/31332) — 21 comments · 3 reactions · open
- **Pull Request** [feat(observability): expose Prisma connection pool saturation metrics](https://github.com/BerriAI/litellm/pull/36607) — 28 comments · 1 reactions · open
- **Issue** [\[Bug\]: Function tools fail with reasoning_effort error for OpenAI gpt-5.6 family models (gpt-5.6-sol/luna/terra) on /chat/completions](https://github.com/BerriAI/litellm/issues/33221) — 11 comments · 3 reactions · closed
- **Pull Request** [feat(newrelic): per-team cost and usage metrics via team callbacks](https://github.com/BerriAI/litellm/pull/37610) — 30 comments · 1 reactions · open
- **Pull Request** [feat(proxy): add POST /auto_router/validate_complexity_router_config to dry-run the complexity-router write gate](https://github.com/BerriAI/litellm/pull/37409) — 25 comments · 1 reactions · closed
- **Issue** [\[Bug\]: Gemini models degenerate in multi-turn tool-calling via /v1/messages — thoughtSignature not propagated from thought parts](https://github.com/BerriAI/litellm/issues/25322) — 2 comments · 5 reactions · open
- **Pull Request** [fix(proxy): run pre-call guardrails on batch input file uploads](https://github.com/BerriAI/litellm/pull/37519) — 22 comments · 1 reactions · closed
- **Pull Request** [fix(proxy): route blocked models through healthy fallbacks](https://github.com/BerriAI/litellm/pull/36672) — 16 comments · 2 reactions · open
- **Issue** [\[BUG\] Virtual key BudgetExceededError uses stale spend while /key/info shows spend below max_budget](https://github.com/BerriAI/litellm/issues/27735) — 10 comments · 1 reactions · open
- **Issue** [\[Feature\]: Azure Entra ID (managed identity) auth for the proxy database](https://github.com/BerriAI/litellm/issues/29661) — 2 comments · 4 reactions · closed
- **Issue** [\[Bug\]: GET /health returns extra_headers and aws_session_token in plaintext](https://github.com/BerriAI/litellm/issues/36898) — 6 comments · 2 reactions · open
- **Pull Request** [fix(oci): make Cohere {{trace}} judges work (re-land #30646, lint-clean)](https://github.com/BerriAI/litellm/pull/30780) — 19 comments · 1 reactions · open
- **Pull Request** [perf(streaming): add shared JSONFragmentAccumulator for Vertex and Anthropic](https://github.com/BerriAI/litellm/pull/36610) — 18 comments · 1 reactions · open
- **Pull Request** [feat(logging): add async_post_call_failure_deployment_hook](https://github.com/BerriAI/litellm/pull/36657) — 19 comments · 1 reactions · open
- **Pull Request** [feat(proxy): enqueued-token rate limiting for batches with refund on completion and cancellation](https://github.com/BerriAI/litellm/pull/37539) — 19 comments · 1 reactions · closed
- **Pull Request** [fix(proxy): make per-model budgets track spend, enforce, and report the same counter](https://github.com/BerriAI/litellm/pull/37736) — 23 comments · 1 reactions · open
- **Issue** [Responses API streaming bridge: multi-step Anthropic tool calls emit text-delta with unregistered chatcmpl- ID](https://github.com/BerriAI/litellm/issues/27671) — 4 comments · 3 reactions · open
- **Pull Request** [feat(proxy): advertise native OIDC client metadata](https://github.com/BerriAI/litellm/pull/35234) — 17 comments · 1 reactions · closed

### [vLLM](https://github.com/vllm-project/vllm)

- **Issue** [\[Feature\]: DeepSeek-V4 Flash sm_80 (A100/A800) support](https://github.com/vllm-project/vllm/issues/40851) — 45 comments · 30 reactions · open
- **Pull Request** [\[Spec Decode\] DFlash2: local convolution + candidate selector](https://github.com/vllm-project/vllm/pull/52816) — 46 comments · 41 reactions · open
- **Pull Request** [\[Core\] Extensible (growable) KV cache](https://github.com/vllm-project/vllm/pull/50779) — 38 comments · 5 reactions · open
- **Pull Request** [\[6/N\]\[KV-Cache Layout Refactor\] Standardize KV cache layout](https://github.com/vllm-project/vllm/pull/51718) — 50 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\]\[Core\]\[Model\] Voxtral realtime: fix boot-OOM / silent-hang / max-len crash on 16 GiB](https://github.com/vllm-project/vllm/pull/45022) — 19 comments · 3 reactions · open
- **Pull Request** [Hybrid KV offload: planner, MultiConnector, and mamba alignment for hybrid models](https://github.com/vllm-project/vllm/pull/38261) — 14 comments · 4 reactions · open
- **Pull Request** [\[Perf\]\[ROCm\] Add AITER custom AG/RS](https://github.com/vllm-project/vllm/pull/48247) — 14 comments · 3 reactions · open
- **Pull Request** [\[Kernel\]\[ROCm\] Cover OCP MX MoE emulation in the mxfp4 oracle test](https://github.com/vllm-project/vllm/pull/43983) — 16 comments · 2 reactions · open
- **Pull Request** [\[Kernel\] FlashInfer CuTe-DSL NVFP4 Quantization](https://github.com/vllm-project/vllm/pull/49775) — 16 comments · 3 reactions · open
- **Pull Request** [\[Bugfix\] Support MistralCommonBackend tokenizers in structured output](https://github.com/vllm-project/vllm/pull/52720) — 46 comments · 2 reactions · closed
- **Pull Request** [\[Kernel\] Single-read fast path for fused RMSNorm + dynamic per-token FP8 quant](https://github.com/vllm-project/vllm/pull/45428) — 14 comments · 3 reactions · open
- **Pull Request** [\[Bugfix\] Fix speculative decoding for short_conv (LFM2) models](https://github.com/vllm-project/vllm/pull/50272) — 30 comments · 4 reactions · open
- **Pull Request** [\[Performance\]\[MLA\] Use FP16 logits for sparse indexer](https://github.com/vllm-project/vllm/pull/52696) — 14 comments · 2 reactions · open
- **Pull Request** [\[Perf\] Integrate flash-maxsim Triton kernels for late-interaction scoring](https://github.com/vllm-project/vllm/pull/40337) — 32 comments · 3 reactions · open
- **Pull Request** [\[WIP\]\[Feature\] A new 2-bit KV cache quantisation backend that cuts 5x memory than FP16 (Oscar-2)](https://github.com/vllm-project/vllm/pull/46774) — 25 comments · 5 reactions · open
- **Pull Request** [Fix async KV loads counting toward scheduler request limit](https://github.com/vllm-project/vllm/pull/42568) — 11 comments · 3 reactions · open
- **Pull Request** [\[Perf\]\[Kernel\] Fused DSA indexer Top-k kernel (LiteTopk)](https://github.com/vllm-project/vllm/pull/48726) — 11 comments · 2 reactions · open
- **Pull Request** [\[Feature\] NVFP4 dispatch for fused RoPE quantization](https://github.com/vllm-project/vllm/pull/46031) — 5 comments · 3 reactions · open
- **Pull Request** [\[XPU\]\[INC\] Add int4 w4a8 (dynamic int8 activation) backend for INC linear layers](https://github.com/vllm-project/vllm/pull/50501) — 33 comments · 2 reactions · open
- **Pull Request** [\[Kernel\]\[Kimi\] fused vision q/k roper kernel](https://github.com/vllm-project/vllm/pull/50400) — 7 comments · 2 reactions · closed
- **Issue** [\[Bug\]: Latest Nightly build with TurboQuant KV cache crashes on large chunked continuation prefill after workspace lock ( testing PR #39931 implementing TQ on Hybrid Attention Models e.g Qwen3.5-9B)](https://github.com/vllm-project/vllm/issues/41726) — 25 comments · 2 reactions · open
- **Pull Request** [\[Frontend\]\[Core\]\[Spec Decode\] Per-request acceptance stats in OpenAI API responses](https://github.com/vllm-project/vllm/pull/48915) — 28 comments · 2 reactions · closed
- **Pull Request** [Add SM90 FA4 Dense and MLA](https://github.com/vllm-project/vllm/pull/51416) — 5 comments · 2 reactions · open
- **Pull Request** [\[ROCm\]\[Perf\] Optimize DeepSeek V4 C4A top-k with AITER](https://github.com/vllm-project/vllm/pull/52882) — 9 comments · 2 reactions · open
- **Issue** [\[Feature\]: Enable LoRA support for tower and connector in more MM models](https://github.com/vllm-project/vllm/issues/31479) — 19 comments · 2 reactions · open
- **Pull Request** [Feat/spec decode under pipeline parallel](https://github.com/vllm-project/vllm/pull/50514) — 26 comments · 2 reactions · open
- **Pull Request** [\[kernel\] Integrate FlashInfer BF16 CuTeDSL Low Latency GEMM](https://github.com/vllm-project/vllm/pull/50572) — 3 comments · 2 reactions · open
- **Pull Request** [\[Kimi-K3\] Extend GEMM-RS to GEMM-AR](https://github.com/vllm-project/vllm/pull/53053) — 6 comments · 2 reactions · open
- **Issue** [\[Performance\]: MTP causes 76% latency regression on Qwen3-Next-80B-A3B-Instruct-FP8](https://github.com/vllm-project/vllm/issues/35387) — 5 comments · 0 reactions · open
- **Pull Request** [\[Model\]\[MoE\] DeepSeek-V4: add opt-in FlashInfer moe_ep expert backend](https://github.com/vllm-project/vllm/pull/49636) — 21 comments · 3 reactions · open

### [SGLang](https://github.com/sgl-project/sglang)

- **Issue** [\[RFC\] Sglang non-GPU process rust migration](https://github.com/sgl-project/sglang/issues/23206) — 10 comments · 11 reactions · open
- **Issue** [\[Tracking\] CI Test Failures and Fixes](https://github.com/sgl-project/sglang/issues/17050) — 13 comments · 10 reactions · open
- **Pull Request** [\[P/D disagg\] Decode-side radix cache for SWA hybrid models (unified radix tree)](https://github.com/sgl-project/sglang/pull/27770) — 42 comments · 4 reactions · closed
- **Pull Request** [\[HiCache\] Fix PP inconsistency with HiCache L3 (#22607)](https://github.com/sgl-project/sglang/pull/27010) — 46 comments · 3 reactions · open
- **Issue** [\[Feature\] Improve Unit Test Coverage](https://github.com/sgl-project/sglang/issues/20865) — 92 comments · 0 reactions · open
- **Issue** [CUDA Coredump Tracker](https://github.com/sgl-project/sglang/issues/26340) — 237 comments · 0 reactions · open
- **Pull Request** [\[Model\] Support Ling-3.0-flash (BailingMoeV3)](https://github.com/sgl-project/sglang/pull/33561) — 8 comments · 9 reactions · open
- **Pull Request** [\[PP&Spec\] enable speculative decoding (eagle_worker_v2) under PP](https://github.com/sgl-project/sglang/pull/31139) — 26 comments · 4 reactions · open
- **Pull Request** [\[DSv4\] Integrate TRT-LLM DSv4 Attention for SM100/103](https://github.com/sgl-project/sglang/pull/30805) — 60 comments · 0 reactions · open
- **Pull Request** [test: switch the Inkling-Small NVFP4 deterministic suite to DSPARK](https://github.com/sgl-project/sglang/pull/35293) — 58 comments · 0 reactions · closed
- **Issue** [CI Maintenance Mode](https://github.com/sgl-project/sglang/issues/21065) — 10 comments · 5 reactions · closed
- **Pull Request** [\[Diffusion\]\[CPU\] Adding AMX optimizations for CPU platform](https://github.com/sgl-project/sglang/pull/30719) — 32 comments · 0 reactions · open
- **Issue** [\[Roadmap\]Fast Engine Recovery: Weight Cache Daemon](https://github.com/sgl-project/sglang/issues/33522) — 5 comments · 5 reactions · open
- **Pull Request** [\[AMD\] Enable gfx1250 Support](https://github.com/sgl-project/sglang/pull/32754) — 22 comments · 1 reactions · open
- **Pull Request** [\[MoE Refactor\] Migrate SM100 trtllm-gen mxfp4 MoE onto MoeRunner](https://github.com/sgl-project/sglang/pull/32405) — 20 comments · 1 reactions · open
- **Pull Request** [TP/PP Consensus checker](https://github.com/sgl-project/sglang/pull/34406) — 4 comments · 5 reactions · closed
- **Pull Request** [\[DO NOT MERGE\] ci](https://github.com/sgl-project/sglang/pull/35708) — 29 comments · 0 reactions · open
- **Pull Request** [\[fmha_v2\] perf: use non-interleaved paged KV input for trtllm sm90/120 prefill](https://github.com/sgl-project/sglang/pull/32272) — 3 comments · 0 reactions · open
- **Pull Request** [\[NPU\] \[Diffusion\] Support MiniMax H3 on Ascend NPU's](https://github.com/sgl-project/sglang/pull/33569) — 23 comments · 0 reactions · open
- **Pull Request** [\[HiCache\] Buffer-only mode for HiCache host memory layer](https://github.com/sgl-project/sglang/pull/34798) — 2 comments · 5 reactions · closed
- **Pull Request** [\[PD\] Introduce runtime role switching between prefill and decode](https://github.com/sgl-project/sglang/pull/28403) — 9 comments · 3 reactions · open
- **Pull Request** [\[XPU\]\[Diffusion\] Enable MiniMax H3 on XPU platforms](https://github.com/sgl-project/sglang/pull/33366) — 21 comments · 0 reactions · open
- **Pull Request** [\[3/N\] elastic-ep: Recapture decode CUDA graphs after scale-up](https://github.com/sgl-project/sglang/pull/33723) — 20 comments · 0 reactions · open
- **Pull Request** [feat(diffusion): add OmniDreams autoregressive video world model](https://github.com/sgl-project/sglang/pull/27442) — 15 comments · 1 reactions · open
- **Pull Request** [\[AMD\] GDN linear out-proj fusion](https://github.com/sgl-project/sglang/pull/28655) — 15 comments · 1 reactions · open
- **Pull Request** [\[Model\] Add LLaDA2.2 Block Routing MoE support](https://github.com/sgl-project/sglang/pull/31768) — 6 comments · 3 reactions · open
- **Pull Request** [\[RFC\] Rust Tree Core Full Component](https://github.com/sgl-project/sglang/pull/32710) — 7 comments · 3 reactions · open
- **Pull Request** [\[AMD\] \[sgl-kernel\] Bypass caches for peer traffic in ROCm custom all-reduce](https://github.com/sgl-project/sglang/pull/32832) — 10 comments · 2 reactions · closed
- **Pull Request** [\[HiCache\] Allow a retraction host pool smaller than the device pool](https://github.com/sgl-project/sglang/pull/35543) — 18 comments · 0 reactions · closed
- **Issue** [\[RFC\]\[Refactor\] `mem_cache` pool / allocator restructure](https://github.com/sgl-project/sglang/issues/25371) — 0 comments · 2 reactions · open

### [Ray](https://github.com/ray-project/ray)

- **Issue** [\[Core\]\[Data\]\[CoreWorker\]Discussion: remaining gRPC thread amplification with many task workers per node](https://github.com/ray-project/ray/issues/64834) — 15 comments · 1 reactions · open
- **Issue** [\[Train\] Share PlacementGroupCleaner across concurrent Train v2 runs](https://github.com/ray-project/ray/issues/65443) — 1 comments · 0 reactions · open
- **Issue** [\[serve\] Support scale-to-zero for gang scheduling](https://github.com/ray-project/ray/issues/65572) — 0 comments · 0 reactions · closed
- **Pull Request** [\[serve\] Columnar zero-copy autoscaling-metrics ingest](https://github.com/ray-project/ray/pull/64281) — 2 comments · 1 reactions · open
- **Pull Request** [\[core\]\[sandbox\] Make Ray Sandbox run Docker-built images out of the box](https://github.com/ray-project/ray/pull/65570) — 1 comments · 5 reactions · closed
- **Issue** [\[Serve\] Orphan ProxyActor left ALIVE when proxy shutdown times out under heavy controller load (blocks worker scale-down)](https://github.com/ray-project/ray/issues/64984) — 7 comments · 0 reactions · open
- **Issue** [\[serve\]\[llm\] KV cache aware routing & management tracker](https://github.com/ray-project/ray/issues/64389) — 8 comments · 0 reactions · open
- **Pull Request** [\[core\]\[joblib\] Add opt-in autoscaling to ray.util.multiprocessing.Pool](https://github.com/ray-project/ray/pull/64957) — 9 comments · 1 reactions · open
- **Pull Request** [\[train\] Share PlacementGroupCleaner across Train runs](https://github.com/ray-project/ray/pull/65447) — 1 comments · 3 reactions · open
- **Issue** [\[Data\] write_lance is incompatible with PyLance 6.x due to removed storage_options_provider argument](https://github.com/ray-project/ray/issues/65129) — 2 comments · 0 reactions · open
- **Issue** [\[Data\] Expose which backpressure policy is blocking an operator in execution diagnostics](https://github.com/ray-project/ray/issues/65607) — 2 comments · 0 reactions · open
- **Pull Request** [\[dashboard\] Configurable defaults + UI dialogs for py-spy/memray profiling params](https://github.com/ray-project/ray/pull/64806) — 7 comments · 1 reactions · open
- **Pull Request** [\[core\] feat(rdt): enable driver-side ray.put with NIXL tensor transport](https://github.com/ray-project/ray/pull/65072) — 6 comments · 1 reactions · open
- **Issue** [Ray logging function not quite working](https://github.com/ray-project/ray/issues/46644) — 5 comments · 0 reactions · open
- **Issue** [\[Core\] - providing `py_executable=uv run` causes failures with unloadable logs](https://github.com/ray-project/ray/issues/54275) — 1 comments · 1 reactions · open
- **Pull Request** [\[Data\] Deduplicate Iceberg read task state](https://github.com/ray-project/ray/pull/64811) — 4 comments · 1 reactions · closed
- **Pull Request** [\[core\]\[dashboard\] Return 4xx from node and actor detail APIs](https://github.com/ray-project/ray/pull/65015) — 5 comments · 1 reactions · open
- **Pull Request** [\[TPU\] Add PyTorch TPU environment variable and runtime_env APIs to Slice and Subslice placement groups](https://github.com/ray-project/ray/pull/65221) — 4 comments · 1 reactions · open
- **Pull Request** [\[llm\]\[ci\] Upgrade to vllm 0.27.0](https://github.com/ray-project/ray/pull/65351) — 5 comments · 1 reactions · open
- **Pull Request** [\[Data\]\[LLM\] Add multi-host TPU batch inference for Ray Data LLM](https://github.com/ray-project/ray/pull/65422) — 4 comments · 1 reactions · open
- **Pull Request** [\[Data\] Add support for writing ORC files](https://github.com/ray-project/ray/pull/65453) — 4 comments · 1 reactions · open
- **Issue** [\[Dashboard\] Ray Dashboard sometimes auto refreshes to point to wrong job id temporarily.](https://github.com/ray-project/ray/issues/45662) — 2 comments · 0 reactions · open
- **Issue** [\[llm\] Promote LLM APIs to beta / stable tracker](https://github.com/ray-project/ray/issues/61248) — 2 comments · 0 reactions · closed
- **Pull Request** [\[serve\] Recover gang context for orphaned replicas to restart the whole gang](https://github.com/ray-project/ray/pull/63208) — 6 comments · 1 reactions · open
- **Pull Request** [\[Feat\]\[Core/Auth\] Enable token authentication for local clusters by default](https://github.com/ray-project/ray/pull/64755) — 2 comments · 1 reactions · open
- **Pull Request** [\[Data\] Add task-based shuffle v2 support for sort](https://github.com/ray-project/ray/pull/64875) — 3 comments · 1 reactions · open
- **Pull Request** [\[Train\] Add NCCL RAS health callback](https://github.com/ray-project/ray/pull/64928) — 2 comments · 1 reactions · open
- **Pull Request** [\[doc\]\[llm\] Add docs for serving LLMs with TPUs](https://github.com/ray-project/ray/pull/65026) — 2 comments · 2 reactions · closed
- **Pull Request** [\[dashboard\] Safely skip unsupported process GPU utilization API](https://github.com/ray-project/ray/pull/65417) — 2 comments · 1 reactions · open
- **Pull Request** [refactor(setup): modernize string formatting and ensure explicit file encoding](https://github.com/ray-project/ray/pull/65439) — 2 comments · 1 reactions · open

### [BentoML](https://github.com/bentoml/BentoML)

- **Pull Request** [feat: agent skills for deploying BentoML services to Kubernetes and EC2](https://github.com/bentoml/BentoML/pull/5683) — 0 comments · 0 reactions · open
- **Pull Request** [fix: Windows tar symlink extraction and fastai CI dependency resolution](https://github.com/bentoml/BentoML/pull/5689) — 0 comments · 0 reactions · open
