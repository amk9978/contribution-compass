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

### [\[Feature\]: Support adding skills to private repos with authentication (SSH key for local, GitHub access token for remote/private)](https://github.com/BerriAI/litellm/issues/26071)

- Project: `BerriAI/litellm`
- Tier: `triage-lead`
- Evidence: Unassigned enhancement with community reactions
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

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

### [\[Docs\] Run pre-commit hooks on doc/source: a per-directory ratchet](https://github.com/ray-project/ray/issues/65427)

- Project: `ray-project/ray`
- Tier: `triage-lead`
- Evidence: Documentation-related issue with no assignee listed
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [LiteLLM](https://github.com/BerriAI/litellm)

- **Issue** [\[Feature\]: Support adding skills to private repos with authentication (SSH key for local, GitHub access token for remote/private)](https://github.com/BerriAI/litellm/issues/26071) — 8 comments · 13 reactions · open
- **Issue** [\[Bug\]: issue while adding Custom MCP server](https://github.com/BerriAI/litellm/issues/23869) — 17 comments · 9 reactions · open
- **Pull Request** [fix(deepseek): DeepSeek V4 support - model registry, multi-turn thinking fix, no-prefix routing](https://github.com/BerriAI/litellm/pull/26660) — 12 comments · 11 reactions · open
- **Issue** [\[Bug\]: LiteLLM_Config table is overwriting newly deployed config](https://github.com/BerriAI/litellm/issues/12875) — 11 comments · 5 reactions · closed
- **Issue** [\[Bug\]: Provider List: https://docs.litellm.ai/docs/providers](https://github.com/BerriAI/litellm/issues/23879) — 6 comments · 6 reactions · open
- **Issue** [\[Bug\]: LiteLLM Proxy - Responses API streaming omits necessary SSE event types](https://github.com/BerriAI/litellm/issues/20975) — 5 comments · 4 reactions · closed
- **Pull Request** [fix(guardrails): scan and re-emit raw Anthropic SSE streams in the bedrock post-call hook](https://github.com/BerriAI/litellm/pull/36598) — 25 comments · 1 reactions · closed
- **Pull Request** [feat(anthropic): add top-level cache_control for automatic prompt cac…](https://github.com/BerriAI/litellm/pull/21784) — 8 comments · 4 reactions · closed
- **Pull Request** [feat(github_copilot): route /v1/messages to Copilot native Anthropic endpoint](https://github.com/BerriAI/litellm/pull/31802) — 12 comments · 3 reactions · closed
- **Issue** [\[Feature\]: Support custom and dynamic headers for A2A Agents](https://github.com/BerriAI/litellm/issues/21409) — 3 comments · 3 reactions · closed
- **Pull Request** [feat(proxy): proactive model deprecation alerts and `/model/deprecations` endpoint](https://github.com/BerriAI/litellm/pull/26900) — 18 comments · 1 reactions · open
- **Pull Request** [feat(tests): Claude Code Compatibility Matrix v0](https://github.com/BerriAI/litellm/pull/28027) — 19 comments · 1 reactions · closed
- **Pull Request** [feat: pre-adoption shadow eval for the auto-router (blind pairwise judge, derived state)](https://github.com/BerriAI/litellm/pull/36587) — 19 comments · 1 reactions · open
- **Issue** [\[Bug\]: litellm oci gemini model tool call issue](https://github.com/BerriAI/litellm/issues/18654) — 8 comments · 1 reactions · closed
- **Pull Request** [fix(caching): guard against None async_redis_conn_pool in RedisCache.disconnect](https://github.com/BerriAI/litellm/pull/31211) — 17 comments · 1 reactions · open
- **Pull Request** [fix(model_prices): add supports_native_structured_output to claude-haiku-4-5 direct API entries](https://github.com/BerriAI/litellm/pull/31221) — 17 comments · 1 reactions · open
- **Pull Request** [feat(ui): manage admin-owned logging destinations](https://github.com/BerriAI/litellm/pull/35517) — 17 comments · 1 reactions · open
- **Pull Request** [fix(proxy): auto-configure PROMETHEUS_MULTIPROC_DIR for multi-worker setups](https://github.com/BerriAI/litellm/pull/20911) — 7 comments · 3 reactions · open
- **Pull Request** [fix(ui): wire bulk invite template download button](https://github.com/BerriAI/litellm/pull/27297) — 10 comments · 2 reactions · open
- **Pull Request** [\[LIT-2877\] Epic A: Cursor SDK agent runtime — /v2/agents, /v2/sessions](https://github.com/BerriAI/litellm/pull/27330) — 14 comments · 1 reactions · closed
- **Pull Request** [fix: honor drop_params in Anthropic pass-through endpoint (#31030)](https://github.com/BerriAI/litellm/pull/31070) — 19 comments · 0 reactions · open
- **Pull Request** [fix: allow safe key type updates for non-admins](https://github.com/BerriAI/litellm/pull/35132) — 15 comments · 1 reactions · open
- **Pull Request** [feat(complexity_router): calibrate the classifier rubric with worked examples, selectable per router](https://github.com/BerriAI/litellm/pull/36578) — 15 comments · 1 reactions · open
- **Issue** [\[Bug\]:  Error: litellm.BadRequestError: ChatgptException - {"detail":"System messages are not allowed"}](https://github.com/BerriAI/litellm/issues/21420) — 4 comments · 1 reactions · closed
- **Issue** [\[Bug\]: Xiaomi MiMo models: 'output_config' parameter causes AsyncCompletions.create() to fail with Claude Code](https://github.com/BerriAI/litellm/issues/24549) — 8 comments · 0 reactions · open
- **Issue** [adaptive_router: one persisted alpha/beta=0 cell bricks the whole router with 500 gammavariate: alpha and beta must be > 0.0](https://github.com/BerriAI/litellm/issues/35590) — 1 comments · 2 reactions · open
- **Pull Request** [fix: allow vllm GET passthrough by checking model in query params](https://github.com/BerriAI/litellm/pull/22104) — 13 comments · 1 reactions · closed
- **Pull Request** [feat(interactions): migrate to Google Interactions API steps schema (May 2026)](https://github.com/BerriAI/litellm/pull/28153) — 13 comments · 1 reactions · closed
- **Pull Request** [fix(mcp): handle integer progress tokens](https://github.com/BerriAI/litellm/pull/32252) — 4 comments · 3 reactions · closed
- **Pull Request** [fix(utils.py): support drop_params for dimensions on Azure and OpenAI compatible embedding calls](https://github.com/BerriAI/litellm/pull/32452) — 12 comments · 1 reactions · open

### [vLLM](https://github.com/vllm-project/vllm)

- **Issue** [\[Bug\]: openai_harmony.HarmonyError: unexpected tokens remaining in message header](https://github.com/vllm-project/vllm/issues/23567) — 47 comments · 24 reactions · open
- **Pull Request** [\[New Model\]\[Nvidia\] Add SM12x support for DeepSeek V4 Flash with essential fixes](https://github.com/vllm-project/vllm/pull/41834) — 440 comments · 40 reactions · open
- **Pull Request** [\[Spec Decode\] DSpark confidence-scheduled verification](https://github.com/vllm-project/vllm/pull/47808) — 41 comments · 12 reactions · closed
- **Issue** [\[Bug\]: MTP speculative decoding crash with illegal memory access on long sequences (Qwen3.6-27B-FP8, v0.19.1)](https://github.com/vllm-project/vllm/issues/40756) — 36 comments · 14 reactions · open
- **Pull Request** [Add Muse Glimmer model support](https://github.com/vllm-project/vllm/pull/51655) — 34 comments · 15 reactions · open
- **Pull Request** [\[Feature\] Enable AITER MXFP4 MoE on gfx942 and optimize tile configurations for MI325X Target Kimi K3 running on MI325X](https://github.com/vllm-project/vllm/pull/50817) — 11 comments · 7 reactions · open
- **Pull Request** [\[Core\] Extensible (growable) KV cache](https://github.com/vllm-project/vllm/pull/50779) — 17 comments · 5 reactions · open
- **Issue** [\[Performance\]: Fully Async Spec-Decoding | Make `seq_lens_cpu` in CommonAttentionMetadata optional](https://github.com/vllm-project/vllm/issues/29134) — 6 comments · 4 reactions · open
- **Issue** [\[Performance\]: Qwen 3.5 27B Prefix Caching](https://github.com/vllm-project/vllm/issues/38988) — 7 comments · 4 reactions · open
- **Issue** [\[RFC\]: Packed Variable Length Speculative Decoding](https://github.com/vllm-project/vllm/issues/47839) — 2 comments · 10 reactions · closed
- **Pull Request** [\[Feature\]\[Whisper\] Native word-level timestamps (cross-attention + DTW)](https://github.com/vllm-project/vllm/pull/47664) — 12 comments · 9 reactions · open
- **Pull Request** [\[Feature\] Mask Replay](https://github.com/vllm-project/vllm/pull/49577) — 33 comments · 3 reactions · closed
- **Pull Request** [\[Model\] Apertus 1.5](https://github.com/vllm-project/vllm/pull/50496) — 13 comments · 8 reactions · open
- **Pull Request** [\[XPU\] Add tuned Mamba SSU configs for Intel Arc Pro B70](https://github.com/vllm-project/vllm/pull/50534) — 12 comments · 2 reactions · closed
- **Pull Request** [\[Kimi-K3\] Add GEMM-RS for sequence parallelism](https://github.com/vllm-project/vllm/pull/52079) — 8 comments · 3 reactions · open
- **Issue** [\[Bug\]: vllm/vllm-openai:latest fails to start Gemma4 with Transformers 5.15.0](https://github.com/vllm-project/vllm/issues/51744) — 14 comments · 5 reactions · open
- **Pull Request** [\[Perf\] Integrate flash-maxsim Triton kernels for late-interaction scoring](https://github.com/vllm-project/vllm/pull/40337) — 29 comments · 3 reactions · open
- **Issue** [\[RFC\]: Support ViT Full CUDA Graph (Tracker)](https://github.com/vllm-project/vllm/issues/38175) — 27 comments · 1 reactions · open
- **Pull Request** [\[Bugfix\] Correct prompt lengths for timed_traces benchmark](https://github.com/vllm-project/vllm/pull/45423) — 3 comments · 3 reactions · open
- **Pull Request** [\[Model\]\[LoRA\] Add tower/connector LoRA support for Ultravox](https://github.com/vllm-project/vllm/pull/48215) — 29 comments · 2 reactions · closed
- **Pull Request** [\[Bugfix\] Add Kimi K3 MoE support to benchmark_moe.py](https://github.com/vllm-project/vllm/pull/50082) — 4 comments · 2 reactions · open
- **Pull Request** [\[Model\]\[Spec Decode\] Tap the pre-norm AttnRes mixture as the Kimi K3 DFlash aux state](https://github.com/vllm-project/vllm/pull/50487) — 24 comments · 3 reactions · open
- **Pull Request** [\[Profiler\] Add Proton CUDA graph attribution](https://github.com/vllm-project/vllm/pull/51084) — 3 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\]\[Helm\] Fix chart resource references](https://github.com/vllm-project/vllm/pull/51664) — 3 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Handle DeepseekV4ForCausalLM in benchmark_moe get_model_params](https://github.com/vllm-project/vllm/pull/52044) — 2 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Add DeepseekV4ForCausalLM to benchmark_moe.py model param dispatch](https://github.com/vllm-project/vllm/pull/52048) — 2 comments · 2 reactions · closed
- **Pull Request** [Add `pydocstyle` to the `ruff` rules](https://github.com/vllm-project/vllm/pull/52136) — 2 comments · 2 reactions · open
- **Pull Request** [\[ModelRunner V2\] Speculative Decoding NGram GPU Implementations](https://github.com/vllm-project/vllm/pull/40704) — 21 comments · 3 reactions · open
- **Pull Request** [\[LoRA\]\[Gemma4\] Support vision tower LoRA](https://github.com/vllm-project/vllm/pull/42662) — 17 comments · 4 reactions · open
- **Pull Request** [\[Core\]\[WIP\] Check for GPU<->CPU sync during CI](https://github.com/vllm-project/vllm/pull/43107) — 21 comments · 3 reactions · open

### [SGLang](https://github.com/sgl-project/sglang)

- **Issue** [DeepSeek V4 Roadmap](https://github.com/sgl-project/sglang/issues/23602) — 74 comments · 29 reactions · open
- **Issue** [\[Roadmap\] sglang auto tuner](https://github.com/sgl-project/sglang/issues/13363) — 13 comments · 29 reactions · open
- **Issue** [\[Roadmap\] Apple Device Support (2026 Q2)](https://github.com/sgl-project/sglang/issues/19137) — 27 comments · 16 reactions · open
- **Issue** [\[Feature\] Kimi K3 Roadmap](https://github.com/sgl-project/sglang/issues/32607) — 8 comments · 22 reactions · open
- **Issue** [\[Feature\] Free-Threaded Python (3.14t / nogil) Support for SGLang](https://github.com/sgl-project/sglang/issues/22889) — 10 comments · 12 reactions · open
- **Issue** [\[Tracking\] CI Test Failures and Fixes](https://github.com/sgl-project/sglang/issues/17050) — 13 comments · 10 reactions · open
- **Pull Request** [Add lyra w4afp8 moe and linear](https://github.com/sgl-project/sglang/pull/8573) — 38 comments · 4 reactions · closed
- **Pull Request** [\[P/D disagg\] Decode-side radix cache for SWA hybrid models (unified radix tree)](https://github.com/sgl-project/sglang/pull/27770) — 38 comments · 3 reactions · open
- **Issue** [\[Feature\] Improve Unit Test Coverage](https://github.com/sgl-project/sglang/issues/20865) — 82 comments · 0 reactions · open
- **Issue** [CUDA Coredump Tracker](https://github.com/sgl-project/sglang/issues/26340) — 232 comments · 0 reactions · open
- **Pull Request** [\[HiCache\] Fix PP inconsistency with HiCache L3 (#22607)](https://github.com/sgl-project/sglang/pull/27010) — 35 comments · 3 reactions · open
- **Pull Request** [\[Model\] Support Ling-3.0-flash (BailingMoeV3)](https://github.com/sgl-project/sglang/pull/33561) — 10 comments · 9 reactions · open
- **Issue** [\[RFC\] Native gRPC Server for SGLang in Rust](https://github.com/sgl-project/sglang/issues/22558) — 8 comments · 7 reactions · open
- **Issue** [\[Feature\] Add KV cache usage prometheus metrics](https://github.com/sgl-project/sglang/issues/5979) — 11 comments · 5 reactions · open
- **Pull Request** [\[Perf\] FlashInfer MLA: remove blocking D2H in spec-decode plan](https://github.com/sgl-project/sglang/pull/27689) — 14 comments · 0 reactions · closed
- **Issue** [\[NVIDIA\] DeepSeek V4 Perf Tracking](https://github.com/sgl-project/sglang/issues/33636) — 8 comments · 5 reactions · open
- **Pull Request** [\[DSv4\] Integrate TRT-LLM DSv4 Attention for SM100/103](https://github.com/sgl-project/sglang/pull/30805) — 36 comments · 0 reactions · open
- **Pull Request** [feat: add cache salt support to KV cache events](https://github.com/sgl-project/sglang/pull/30827) — 30 comments · 0 reactions · closed
- **Pull Request** [\[Perf\] Occupancy tuning for DSA indexer fp8-quant Q kernel](https://github.com/sgl-project/sglang/pull/32755) — 31 comments · 0 reactions · closed
- **Pull Request** [\[AMD\] Fuse shared_expert_gate GEMV into the MoE append kernel (HIP/aiter)](https://github.com/sgl-project/sglang/pull/28666) — 25 comments · 1 reactions · open
- **Pull Request** [\[AMD\]\[Quantization\] Online MXFP4 quantization 4/N - NVFP4 to MXFP4 Online Requantization on AMD GPUs](https://github.com/sgl-project/sglang/pull/29328) — 24 comments · 1 reactions · open
- **Pull Request** [\[do not merge\] check result of CI](https://github.com/sgl-project/sglang/pull/30691) — 28 comments · 0 reactions · open
- **Pull Request** [Support XQA backend for SpecDec verify](https://github.com/sgl-project/sglang/pull/32269) — 4 comments · 0 reactions · open
- **Issue** [\[Bug\] Long DeepGEMM v2 warmup time in latest SGLang leading to NCCL timeout.](https://github.com/sgl-project/sglang/issues/9867) — 18 comments · 0 reactions · closed
- **Pull Request** [\[FlashInfer v0.6.16\] Support FlashInfer CuTe DSL NVFP4 MoE quantization](https://github.com/sgl-project/sglang/pull/28354) — 26 comments · 0 reactions · open
- **Pull Request** [\[HiCache\]: Optimize hybrid/DSA L3 prefetch result sync and usable-prefix clamping](https://github.com/sgl-project/sglang/pull/31443) — 20 comments · 1 reactions · closed
- **Pull Request** [\[Bug Fix\] Sync FlashInfer autotune tactic selection across TP ranks](https://github.com/sgl-project/sglang/pull/23317) — 22 comments · 0 reactions · open
- **Pull Request** [\[BugFix\] Fix race in c128 prefill plan kernel on ragged extend](https://github.com/sgl-project/sglang/pull/32467) — 23 comments · 0 reactions · closed
- **Pull Request** [\[NVIDIA\]\[comm\] Merge EP+MoE-TP post-experts all-reduces into one _TP reduction](https://github.com/sgl-project/sglang/pull/32963) — 22 comments · 0 reactions · open
- **Pull Request** [\[AMD\] Add fused all-reduce RMSNorm per-token FP8/MXFP4 quant](https://github.com/sgl-project/sglang/pull/29723) — 13 comments · 2 reactions · open

### [Ray](https://github.com/ray-project/ray)

- **Issue** [\[core\] Ray session conflicts with PyArrow+HDFS](https://github.com/ray-project/ray/issues/36415) — 27 comments · 4 reactions · open
- **Issue** [\[Umbrella\] Ray Sandboxing with gVisor](https://github.com/ray-project/ray/issues/65352) — 7 comments · 2 reactions · open
- **Issue** [\[Data/LLM\] Non stop CPU autoscaling with vLLM](https://github.com/ray-project/ray/issues/56431) — 11 comments · 0 reactions · open
- **Issue** [\[serve\]\[llm\] Governance middleware layer for Ray Serve LLM — PII detection, cost budgets, policy enforcement, and audit trails](https://github.com/ray-project/ray/issues/65259) — 9 comments · 0 reactions · open
- **Issue** [\[Data\] read_webdataset emits one DataFrame per sample, causing per-sample size_bytes overhead in the output buffer](https://github.com/ray-project/ray/issues/65350) — 1 comments · 0 reactions · closed
- **Issue** [\[data\] Fair-share allocation overstates runnable task-pool demand](https://github.com/ray-project/ray/issues/65433) — 0 comments · 0 reactions · open
- **Issue** [\[data\] BlockOutputBuffer rebuilds the remainder for every row-sized output](https://github.com/ray-project/ray/issues/65434) — 0 comments · 0 reactions · open
- **Issue** [\[Train\] Share PlacementGroupCleaner across concurrent Train v2 runs](https://github.com/ray-project/ray/issues/65443) — 0 comments · 0 reactions · open
- **Pull Request** [\[Core\] Mobilint Accelerator Support](https://github.com/ray-project/ray/pull/61898) — 7 comments · 3 reactions · open
- **Pull Request** [\[core\] Add opt-in swap accounting to memory monitor and scheduler](https://github.com/ray-project/ray/pull/63793) — 10 comments · 1 reactions · open
- **Issue** [\[Core\] Removing an in-flight placement group can leak prepared bundles and block later placement groups](https://github.com/ray-project/ray/issues/64693) — 2 comments · 0 reactions · open
- **Issue** [\[Data\] ObjectRefs passed to map UDFs through `fn_args` are not dereferenced](https://github.com/ray-project/ray/issues/65449) — 3 comments · 0 reactions · open
- **Pull Request** [\[data\] Add orc datasource for V2](https://github.com/ray-project/ray/pull/64540) — 7 comments · 1 reactions · open
- **Pull Request** [\[doc\]\[KubeRay\] Add mTLS for RayClusters user guide](https://github.com/ray-project/ray/pull/65107) — 7 comments · 1 reactions · open
- **Pull Request** [\[core\] Enable TCP keepalive on GCS<->Redis connections](https://github.com/ray-project/ray/pull/65424) — 2 comments · 2 reactions · open
- **Pull Request** [\[docs\] vendor the KubeRay CRD API reference into the Ray docs](https://github.com/ray-project/ray/pull/65428) — 6 comments · 1 reactions · open
- **Issue** [\[Data\] OpTask._cancel never passes force=True](https://github.com/ray-project/ray/issues/65280) — 1 comments · 0 reactions · open
- **Issue** [The task_id/put_index contract in `GetGeneratorReturnId` is unenforced (the RAY_CHECK is a tautology)](https://github.com/ray-project/ray/issues/65300) — 0 comments · 0 reactions · closed
- **Issue** [\[Docs\] Run pre-commit hooks on doc/source: a per-directory ratchet](https://github.com/ray-project/ray/issues/65427) — 0 comments · 0 reactions · open
- **Issue** [\[Core\] Randomize worker port allocation to reduce deterministic collisions between raylets](https://github.com/ray-project/ray/issues/65444) — 0 comments · 0 reactions · open
- **Issue** [\[Core\]\[runtime_env\] RuntimeEnv agent leaks one logger (and its file descriptors) per job, eventually failing all setups with EMFILE`](https://github.com/ray-project/ray/issues/65451) — 0 comments · 0 reactions · open
- **Issue** [\[Core\]\[KubeRay\] Autoscaler sends all log records, including INFO, to stderr](https://github.com/ray-project/ray/issues/65454) — 0 comments · 0 reactions · open
- **Pull Request** [\[Data\]\[1/N\] add external shuffle runtime library](https://github.com/ray-project/ray/pull/64828) — 4 comments · 1 reactions · open
- **Pull Request** [fix(autoscaler): deduplicate cloud instances during termination](https://github.com/ray-project/ray/pull/65419) — 0 comments · 2 reactions · open
- **Pull Request** [\[WIP\]\[serve\] Use `ObjectRefGenerator._get_next_ref_n` to avoid blocking on `_to_object_ref`](https://github.com/ray-project/ray/pull/64451) — 2 comments · 1 reactions · closed
- **Pull Request** [\[Data\] Fix ResourceBudget backpressure causing pipeline stall](https://github.com/ray-project/ray/pull/64601) — 2 comments · 1 reactions · open
- **Pull Request** [\[Autoscaler\]\[AWS\] Retry key pair creation after duplicate](https://github.com/ray-project/ray/pull/64738) — 2 comments · 1 reactions · open
- **Pull Request** [\[Train\] Add NCCL RAS health callback](https://github.com/ray-project/ray/pull/64928) — 2 comments · 1 reactions · open
- **Pull Request** [\[core\]\[dashboard\] Return 4xx from node and actor detail APIs](https://github.com/ray-project/ray/pull/65015) — 3 comments · 1 reactions · open
- **Pull Request** [\[Serve\] Optimize RollingWindow metrics using monotonic deque in O(1)](https://github.com/ray-project/ray/pull/65031) — 2 comments · 1 reactions · open

### [BentoML](https://github.com/bentoml/BentoML)

- **Pull Request** [fix(server): retain CapacityLimiter slot until worker thread completes (#5642)](https://github.com/bentoml/BentoML/pull/5671) — 4 comments · 0 reactions · open
- **Pull Request** [fix(sdk): check generic args length on bare iterator return annotations to avoid IndexError](https://github.com/bentoml/BentoML/pull/5643) — 3 comments · 0 reactions · open
- **Pull Request** [docs: note OpenAI client base_url for multi-model gateways](https://github.com/bentoml/BentoML/pull/5681) — 1 comments · 0 reactions · closed
