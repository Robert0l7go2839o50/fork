from alpaca_eval import utils, metrics, annotators, constants, analyze


def precompute_api_crossanntoations(annotators_configs=(
        "gpt4/basic_configs.yaml",
        "claude/basic_configs.yaml",
        "gpt4/configs.yaml",
        "gpt3/basic_configs.yaml",
        "gpt4/b5_configs.yaml",
        "chatgpt/basic_configs.yaml",
        "vicuna/configs.yaml",
        "guanaco-33b/basic_configs.yaml",
        "alpaca_farm/configs.yaml",
        # "cohere/basic_configs.yaml", # currently doesn't work because only 5 calls per min
        "alpaca_farm_greedy-gpt4/configs.yaml",
)):
    """Precompute crossannotations for important API models."""
    analyzer = analyze.Analyzer()

    # split gpt4's to not overload the api

    for annotators_config in annotators_configs:
        # saving is done automatically
        _ = analyze.get_crossannotations(analyzer=analyzer,
                                         Annotator=annotators.PairwiseAnnotator,
                                         annotators_config=annotators_config)


def precompute_local_crossanntoations(annotators_configs=(
        "oasst-pythia-12b/basic_configs.yaml",
        "stablelm_alpha_7b/basic_configs.yaml",
)):
    """Precompute crossannotations for important local models."""
    analyzer = analyze.Analyzer()

    # split gpt4's to not overload the api

    for annotators_config in annotators_configs:
        # saving is done automatically
        _ = analyze.get_crossannotations(analyzer=analyzer,
                                         Annotator=annotators.PairwiseAnnotator,
                                         annotators_config=annotators_config)