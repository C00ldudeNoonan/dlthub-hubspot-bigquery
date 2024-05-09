from dagster import (
    AssetExecutionContext,
    AutoMaterializePolicy,
    AutoMaterializeRule,
    SourceAsset,
    file_relative_path,
)
from dagster._annotations import public
from typing import Optional
from dagster_embedded_elt.dlt import (
    DagsterDltResource,
    DagsterDltTranslator,
    dlt_assets,
)
from dlt import pipeline
from dlt.extract.resource import DltResource
from dlt_sources.hubspot import hubspot

dlt_resource = DagsterDltResource()


class HubspotDagsterDltTranslator(DagsterDltTranslator):
    @public
    def get_auto_materialize_policy(self, resource: DltResource) -> Optional[AutoMaterializePolicy]:
        return AutoMaterializePolicy.eager().with_rules(
            AutoMaterializeRule.materialize_on_cron("0 0 * * *")
        )


@dlt_assets(
    dlt_source=hubspot(include_history=True),
    dlt_pipeline=pipeline(
        pipeline_name="hubspot",
        destination="bigquery",
        dataset_name="hubspot_dataset"
    ),
    name="hubspot",
    group_name="hubspot_noonan_labs",
    dlt_dagster_translator=HubspotDagsterDltTranslator(),
)
def hubspot_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)


