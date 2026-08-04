from personadna.pipeline.pipeline_runner import PipelineRunner


def test_pipeline_runner():

    runner = PipelineRunner()

    persona = runner.process(
        source="demo",
        object_type="text",
        content="Hello PersonaDNA",
    )

    assert persona.name == "Generated Persona"

    assert len(persona.observations) == 1

    assert len(persona.relationships) == 0
