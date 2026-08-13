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

- **Pull Request** [feat(cost): support time-based off-peak pricing in cost calculation](https://github.com/BerriAI/litellm/pull/31725) — 15 comments · 2 reactions · open
- **Issue** [\[Feature\]: Support time-based / peak-offpeak pricing for model cost calculation](https://github.com/BerriAI/litellm/issues/31606) — 1 comments · 2 reactions · open
- **Issue** [OpenAPI→MCP tool generation drops request body schema when it uses $ref (FastAPI/Pydantic specs)](https://github.com/BerriAI/litellm/issues/36765) — 3 comments · 0 reactions · open
- **Pull Request** [feat(skills): self-service skill submission with admin review](https://github.com/BerriAI/litellm/pull/36677) — 7 comments · 1 reactions · open
- **Pull Request** [fix(mcp): expose client HTTP headers to logging callbacks and hooks](https://github.com/BerriAI/litellm/pull/36724) — 7 comments · 1 reactions · open
- **Pull Request** [refactor(ui): migrate guardrails-monitor, projects, logs to shadcn](https://github.com/BerriAI/litellm/pull/34606) — 4 comments · 1 reactions · closed
- **Pull Request** [fix(vertex batches): reject vertex_location='global' up front](https://github.com/BerriAI/litellm/pull/35366) — 5 comments · 1 reactions · open
- **Pull Request** [fix(proxy): guard optional prisma import in DB exception classifiers](https://github.com/BerriAI/litellm/pull/35458) — 4 comments · 1 reactions · open
- **Pull Request** [fix(bedrock): route knowledge base ingestion to control plane](https://github.com/BerriAI/litellm/pull/36771) — 5 comments · 1 reactions · open
- **Pull Request** [fix(bedrock): drop trailing empty Converse chunk](https://github.com/BerriAI/litellm/pull/36783) — 4 comments · 1 reactions · open
- **Pull Request** [fix(datadog_llm_obs): map tool_calls to DD Message schema and cache tokens to span metrics](https://github.com/BerriAI/litellm/pull/35946) — 7 comments · 1 reactions · open
- **Pull Request** [fix(utils): register_model with an empty payload silently turns unknown-model cost errors into $0.0](https://github.com/BerriAI/litellm/pull/36561) — 3 comments · 1 reactions · open
- **Pull Request** [fix(streaming): dict-usage arm drops prompt_tokens_details/completion_tokens_details its sibling arms preserve](https://github.com/BerriAI/litellm/pull/36678) — 3 comments · 1 reactions · open
- **Pull Request** [refactor(ui): migrate guardrails content tables to shared DataTable](https://github.com/BerriAI/litellm/pull/36708) — 3 comments · 1 reactions · closed
- **Pull Request** [feat(ui): add user ID request log filter](https://github.com/BerriAI/litellm/pull/36781) — 3 comments · 1 reactions · open
- **Issue** [When using local ollama model getting the error](https://github.com/BerriAI/litellm/issues/36786) — 0 comments · 0 reactions · open
- **Issue** [\[bug\]: proxy uses request-body api_key without allow_client_side_credentials](https://github.com/BerriAI/litellm/issues/36794) — 0 comments · 0 reactions · open
- **Pull Request** [feat(nebius): add model pricing metadata](https://github.com/BerriAI/litellm/pull/33185) — 5 comments · 1 reactions · open
- **Pull Request** [refactor(ui): migrate usage tables to shared DataTable](https://github.com/BerriAI/litellm/pull/36707) — 1 comments · 1 reactions · closed
- **Pull Request** [refactor(ui): migrate guardrails monitor table to shared DataTable](https://github.com/BerriAI/litellm/pull/36709) — 1 comments · 1 reactions · closed
- **Pull Request** [ci: promote staging to main](https://github.com/BerriAI/litellm/pull/36725) — 5 comments · 0 reactions · closed
- **Pull Request** [fix(responses): raise on failed chat streams](https://github.com/BerriAI/litellm/pull/36782) — 5 comments · 0 reactions · open
- **Pull Request** [fix(router): support anthropic messages streaming fallback](https://github.com/BerriAI/litellm/pull/36791) — 4 comments · 1 reactions · open
- **Pull Request** [feat(gemini): day-0 pricing for gemini-3.7-flash](https://github.com/BerriAI/litellm/pull/36792) — 4 comments · 1 reactions · closed
- **Pull Request** [fix(nebius): route requests to Token Factory](https://github.com/BerriAI/litellm/pull/36777) — 3 comments · 0 reactions · open
- **Pull Request** [fix(model_prices): refresh deprecation dates, add grok-4.6 and gemini 3.1 flash tts](https://github.com/BerriAI/litellm/pull/36788) — 3 comments · 1 reactions · open
- **Pull Request** [test(e2e): assert the model allow-list permits, not only denies](https://github.com/BerriAI/litellm/pull/36795) — 2 comments · 1 reactions · open
- **Pull Request** [feat(guardrails/xecguard): pass the calling virtual key through xecguard to the SIEM (splunk)](https://github.com/BerriAI/litellm/pull/36797) — 2 comments · 1 reactions · open
- **Pull Request** [fix(ui): make per-user usage filter searchable](https://github.com/BerriAI/litellm/pull/36790) — 1 comments · 1 reactions · open
- **Pull Request** [refactor(ui): migrate SectionHeader and ToolsSection to shadcn](https://github.com/BerriAI/litellm/pull/36793) — 1 comments · 1 reactions · open

### [vLLM](https://github.com/vllm-project/vllm)

- **Pull Request** [\[New Model\]\[Nvidia\] Add SM12x support for DeepSeek V4 Flash with essential fixes](https://github.com/vllm-project/vllm/pull/41834) — 441 comments · 41 reactions · open
- **Pull Request** [\[Perf\] Integrate flash-maxsim Triton kernels for late-interaction scoring](https://github.com/vllm-project/vllm/pull/40337) — 30 comments · 3 reactions · open
- **Pull Request** [\[Bugfix\] Add Kimi K3 MoE support to benchmark_moe.py](https://github.com/vllm-project/vllm/pull/50082) — 4 comments · 2 reactions · open
- **Pull Request** [\[Core\]\[WIP\] Check for GPU<->CPU sync during CI](https://github.com/vllm-project/vllm/pull/43107) — 23 comments · 3 reactions · open
- **Pull Request** [\[ROCm\] Defer `tilelang` import through its import `from vllm.tilelang_utils import tilelang` and relaxed `has_tilelang`](https://github.com/vllm-project/vllm/pull/51159) — 26 comments · 2 reactions · open
- **Pull Request** [\[K3\] support recoverssm for K3](https://github.com/vllm-project/vllm/pull/51855) — 2 comments · 2 reactions · open
- **Pull Request** [Add `pydocstyle` to the `ruff` rules](https://github.com/vllm-project/vllm/pull/52136) — 2 comments · 2 reactions · open
- **Pull Request** [\[Formatting\] Collapse multi-line arg lists where possible](https://github.com/vllm-project/vllm/pull/43449) — 5 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Fix MiniMax M3 prompt reasoning initialization](https://github.com/vllm-project/vllm/pull/50594) — 24 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\] Restore multimodal support on the plain "vllm" throughput backend](https://github.com/vllm-project/vllm/pull/52168) — 1 comments · 2 reactions · open
- **Pull Request** [\[5/N\]\[KV-Cache Layout Refactor\] Backend-published KV packing via customize_spec](https://github.com/vllm-project/vllm/pull/51704) — 23 comments · 2 reactions · open
- **Pull Request** [\[ROCm\]\[CI\] Gating more ROCm tests](https://github.com/vllm-project/vllm/pull/44969) — 18 comments · 2 reactions · open
- **Issue** [\[Bug\]: Decode Context Parallelism (`--decode-context-parallel-size`) output drift and gibberish in v0.21.0 and latest nightly](https://github.com/vllm-project/vllm/issues/41623) — 20 comments · 0 reactions · open
- **Pull Request** [\[ModelOpt\] Redesign the LinearMethod classes using the generic QuantKey-driven method](https://github.com/vllm-project/vllm/pull/49381) — 18 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\]\[Spec Decode\] Fix autoregressive draft decode capture with dynamic SD](https://github.com/vllm-project/vllm/pull/49652) — 11 comments · 3 reactions · open
- **Pull Request** [\[Spec Decode\]\[Perf\] Fuse the MTP trailing all-reduce; local-argmax draft tokens](https://github.com/vllm-project/vllm/pull/49793) — 15 comments · 2 reactions · open
- **Pull Request** [\[Bugfix\]\[Mamba\] Fix overlapping state copy race](https://github.com/vllm-project/vllm/pull/50729) — 15 comments · 2 reactions · open
- **Issue** [\[Bug\]: draft_model speculative decoding crashes at init under TP>1 when draft hidden_size > target (TRT-LLM fused allreduce+RMSNorm workspace sized from target only)](https://github.com/vllm-project/vllm/issues/52023) — 5 comments · 2 reactions · open
- **Pull Request** [\[ROCm\] Pad non-aligned AITER MLA heads](https://github.com/vllm-project/vllm/pull/51647) — 13 comments · 2 reactions · open
- **Issue** [\[Perf\] DSD arms pay a large baseline tax vs no-spec under production defaults; PIECEWISE override identified as one factor](https://github.com/vllm-project/vllm/issues/49986) — 10 comments · 0 reactions · open
- **Issue** [\[Bug\] v0.27.0 engine permanently stalls after ~1 min idle on 4-node TP=4 (GB10/sm_121, aarch64): shm_broadcast writer starves, requests never reach scheduler](https://github.com/vllm-project/vllm/issues/51921) — 11 comments · 0 reactions · open
- **Pull Request** [\[ROCm\] Add per-call decode budget to sparse-MLA indexer](https://github.com/vllm-project/vllm/pull/43327) — 7 comments · 3 reactions · open
- **Issue** [\[Performance\]: Dynamic speculative decoding (num_speculative_tokens_per_batch_size) causes catastrophic aggregate-throughput collapse under concurrency at the batch-size threshold (MTP, V1/PIECEWISE)](https://github.com/vllm-project/vllm/issues/49548) — 8 comments · 0 reactions · open
- **Pull Request** [\[ModelRunnerV2\] Support prompt embeds](https://github.com/vllm-project/vllm/pull/42963) — 13 comments · 1 reactions · open
- **Pull Request** [\[Model Runner V2\]\[Spec Decode\] Support spec decode with draft model](https://github.com/vllm-project/vllm/pull/43091) — 9 comments · 2 reactions · open
- **Pull Request** [Fix sparse BlockStored event token/hash mapping](https://github.com/vllm-project/vllm/pull/44488) — 13 comments · 2 reactions · open
- **Pull Request** [\[Frontend\]  Support count_reasoning_tokens in the Streaming Parser Engine](https://github.com/vllm-project/vllm/pull/45802) — 8 comments · 2 reactions · open
- **Issue** [\[Bug\]: speculative decoding under pipeline parallelism produces wrong output with --no-async-scheduling](https://github.com/vllm-project/vllm/issues/52071) — 6 comments · 0 reactions · open
- **Pull Request** [\[Kernel\] Warm up hybrid GDN/Mamba/MRoPE kernels](https://github.com/vllm-project/vllm/pull/43642) — 11 comments · 2 reactions · open
- **Pull Request** [\[EC Connector\] Added Build Connector Worker Meta for EC Connector](https://github.com/vllm-project/vllm/pull/49585) — 7 comments · 2 reactions · open

### [SGLang](https://github.com/sgl-project/sglang)

- **Issue** [\[Agentic Inference\] Programmatic KV Cache for Agentic Workloads](https://github.com/sgl-project/sglang/issues/27574) — 19 comments · 15 reactions · open
- **Issue** [\[Tracking\] CI Test Failures and Fixes](https://github.com/sgl-project/sglang/issues/17050) — 13 comments · 10 reactions · open
- **Pull Request** [\[P/D disagg\] Decode-side radix cache for SWA hybrid models (unified radix tree)](https://github.com/sgl-project/sglang/pull/27770) — 38 comments · 3 reactions · open
- **Pull Request** [\[DSV4\] Enable overlap scheduling for online C128 MTP](https://github.com/sgl-project/sglang/pull/30497) — 8 comments · 1 reactions · open
- **Pull Request** [\[AMD\]\[Quantization\] Online MXFP4 quantization 4/N - NVFP4 to MXFP4 Online Requantization on AMD GPUs](https://github.com/sgl-project/sglang/pull/29328) — 22 comments · 1 reactions · open
- **Pull Request** [\[MoE Refactor\] Migrate SM100 trtllm-gen mxfp4 MoE onto MoeRunner](https://github.com/sgl-project/sglang/pull/32405) — 17 comments · 1 reactions · open
- **Pull Request** [\[AMD\] Add dense-FP8 for MXFP4 checkpoints with fused silu, mul, activation quant](https://github.com/sgl-project/sglang/pull/28932) — 15 comments · 0 reactions · open
- **Pull Request** [\[AMD\] \[Docker\] Upgrade Python 3.12 + torch 2.11 + triton 3.7 in ROCm 7.2.4](https://github.com/sgl-project/sglang/pull/30984) — 15 comments · 0 reactions · open
- **Pull Request** [add fid accuracy benchmark for sglang diffusion t2i model](https://github.com/sgl-project/sglang/pull/25871) — 6 comments · 1 reactions · open
- **Pull Request** [\[NPU\] Add mxfp4-w4a8 MOE Quantization Support for NPU](https://github.com/sgl-project/sglang/pull/30318) — 11 comments · 0 reactions · open
- **Issue** [\[Tracking\] PD disaggregation shared-protocol unification](https://github.com/sgl-project/sglang/issues/34510) — 5 comments · 0 reactions · open
- **Pull Request** [\[XPU\] upgrade sglang xpu backend to PyTorch 2.13](https://github.com/sgl-project/sglang/pull/31751) — 7 comments · 0 reactions · open
- **Issue** [\[Feature\] Router GEMM should keep fp32 output under deterministic inference (DeepSeek V3/V4)](https://github.com/sgl-project/sglang/issues/34758) — 0 comments · 0 reactions · open
- **Pull Request** [Avoid materializing GDN QKV tensors during target verification](https://github.com/sgl-project/sglang/pull/33778) — 5 comments · 0 reactions · open
- **Pull Request** [\[Perf\] Skip trivial DSV4 nonpaged indexer logits](https://github.com/sgl-project/sglang/pull/33857) — 5 comments · 0 reactions · open
- **Pull Request** [\[PD\] Add the missing Prefill bootstrap timeout for NIXL](https://github.com/sgl-project/sglang/pull/34692) — 4 comments · 0 reactions · closed
- **Pull Request** [Retain SWA down to the last state checkpoint](https://github.com/sgl-project/sglang/pull/34729) — 5 comments · 0 reactions · open
- **Pull Request** [\[sglang-miles\] RDT/NIXL weight sync support for Ray scheduler actors](https://github.com/sgl-project/sglang/pull/27723) — 2 comments · 0 reactions · open
- **Pull Request** [\[HiCache\] fix: resolve Mooncake local_hostname per node for runtime attach](https://github.com/sgl-project/sglang/pull/29668) — 7 comments · 0 reactions · open
- **Pull Request** [\[Intel\]\[XPU\]\[LoRA\] Enable LoRA on Intel XPU](https://github.com/sgl-project/sglang/pull/30345) — 3 comments · 0 reactions · open
- **Pull Request** [feat(kv-events): Add component_types field to BlockStored for per-component placement tracking](https://github.com/sgl-project/sglang/pull/32514) — 2 comments · 1 reactions · open
- **Pull Request** [\[AMD\] Don't request the unused softmax LSE in the AITER diffusion backend](https://github.com/sgl-project/sglang/pull/32926) — 2 comments · 0 reactions · open
- **Pull Request** [\[NPU CI\] Reorganize test output/log directory structure with workflow context](https://github.com/sgl-project/sglang/pull/33685) — 2 comments · 0 reactions · open
- **Pull Request** [fix: make Cache-DiT actually cache on MiniMax-H3](https://github.com/sgl-project/sglang/pull/33827) — 3 comments · 0 reactions · closed
- **Pull Request** [\[HiCache\] Route --file-storage-path to the file storage backend](https://github.com/sgl-project/sglang/pull/33883) — 3 comments · 0 reactions · open
- **Pull Request** [Publish per-scheduler load on a dedicated socket for load-aware routers](https://github.com/sgl-project/sglang/pull/34608) — 2 comments · 0 reactions · open
- **Pull Request** [Widen swapAB dispatch range in SM120 fp8 blockwise GEMM](https://github.com/sgl-project/sglang/pull/34731) — 2 comments · 0 reactions · open
- **Pull Request** [\[Diffusion\] Unify component residency controls](https://github.com/sgl-project/sglang/pull/34736) — 2 comments · 0 reactions · open
- **Pull Request** [Fix Qwen3.5 ModelOpt NVFP4 checkpoint loading](https://github.com/sgl-project/sglang/pull/28929) — 0 comments · 1 reactions · open
- **Pull Request** [\[Feature\] MXFP4 KV Cache Decode for DSV4 on Hopper](https://github.com/sgl-project/sglang/pull/32741) — 1 comments · 0 reactions · open

### [Ray](https://github.com/ray-project/ray)

- **Issue** [Ray Dashboard is susceptible to a Local File Inclusion bug with default settings](https://github.com/ray-project/ray/issues/45751) — 9 comments · 0 reactions · closed
- **Issue** [\[Core\] Provide a way to disable the worker-log `(pid=…)` prefix without disabling driver forwarding or overriding the root logger](https://github.com/ray-project/ray/issues/64992) — 6 comments · 0 reactions · open
- **Pull Request** [\[train\] Share PlacementGroupCleaner across Train runs](https://github.com/ray-project/ray/pull/65447) — 0 comments · 2 reactions · open
- **Pull Request** [\[Train\] Add NCCL RAS health callback](https://github.com/ray-project/ray/pull/64928) — 2 comments · 1 reactions · open
- **Pull Request** [\[docs\] Add Kubernetes and KubeRay conventions to the style guide](https://github.com/ray-project/ray/pull/65239) — 3 comments · 1 reactions · open
- **Issue** [\[serve\] Enable mypy type checking on ray/serve to catch real production bugs (e.g. the rank-corruption bug in #64181)](https://github.com/ray-project/ray/issues/64643) — 1 comments · 0 reactions · open
- **Pull Request** [\[doc\]\[History server\] Update doc for history server for `RAY_ROOT_DIR` -> `STORAGE_ROOT_DIR`](https://github.com/ray-project/ray/pull/65441) — 1 comments · 1 reactions · open
- **Pull Request** [\[Data\] Add support for writing ORC files](https://github.com/ray-project/ray/pull/65453) — 1 comments · 1 reactions · open
- **Pull Request** [\[doc\] Render the Jobs API spec with sphinxcontrib-openapi instead of ReDoc](https://github.com/ray-project/ray/pull/65460) — 0 comments · 1 reactions · open
- **Pull Request** [\[core\] feat(rdt): enable driver-side ray.put with NIXL tensor transport](https://github.com/ray-project/ray/pull/65072) — 2 comments · 1 reactions · open
- **Pull Request** [\[docs\] Sync the vendored KubeRay CRD API reference](https://github.com/ray-project/ray/pull/65462) — 0 comments · 1 reactions · open
- **Pull Request** [core: release runtime env per-job loggers](https://github.com/ray-project/ray/pull/65463) — 0 comments · 1 reactions · open

### [BentoML](https://github.com/bentoml/BentoML)

No new or materially changed signals.
