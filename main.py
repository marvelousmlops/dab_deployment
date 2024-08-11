from my_package.example import hello_you
from loguru import logger
from adplogger.utils import configure_adplogger, ADPLoggerConfig
import yaml
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root_path",
        action="store",
        default=None,
        type=str,
        required=True,
    )

    args = parser.parse_args()
    root_path = args.root_path

    with open(f"/Workspace/{root_path}/files/name.yml", "r") as file:
        config = yaml.safe_load(file)
    hello_you(config['name'])
    

    logger_config = ADPLoggerConfig(

        # The default extra fields to be added to every log record. Those are examples.
        default_extra={
            "env": "dev",
            "opco": "cz", #To be added
            "data_product": "mydataproduct",
            "adf_pipeline": "aggregate_daily",
            "adf_run_uuid": "00000000-0000-0000-0000-000000000000"},
    )

    configure_adplogger(logger_config)

    logger.info("Log message")