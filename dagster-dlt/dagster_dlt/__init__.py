from dagster import Definitions, load_assets_from_modules

from .assets import dlt
from dagster_embedded_elt.dlt import DagsterDltResource

dlt_resource = DagsterDltResource()


defs = Definitions(
    assets=[
        dlt.hubspot_assets,
    ],
    resources={
        "dlt": dlt_resource,
    },
)
