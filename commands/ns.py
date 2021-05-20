from typing import Dict, Iterator

import click
from kubernetes import client, config

from utils.echo import echo_dict, echo_table


def get_namespaces() -> Iterator[str]:
    """Iterator of list of namespaces"""
    config.load_kube_config()
    for namespace in client.CoreV1Api().list_namespace().items:
        if namespace.metadata:
            yield namespace.metadata.name


def get_namespace_info(namespace: str) -> Dict[str, str]:
    """Returns selected propertiers of namespace"""
    config.load_kube_config()
    ns = client.CoreV1Api().read_namespace(namespace)

    return {
        "name": ns.metadata.name,
        "created": ns.metadata.creation_timestamp.strftime("%Y/%m/%d %H:%M:%S"),
        "uid": ns.metadata.uid,
    }


@click.group("ns")
def cmd_ns():
    """Show and manage namespaces"""
    pass


@cmd_ns.command("get")
@click.argument("namespace", required=False)
@click.option("--info", is_flag=True, help="Show only namespace info")
def cmd_get(namespace: str = None, info: bool = False):
    """Display a list of usable namespaces, or components on the namespace"""
    contexts, active_context = config.list_kube_config_contexts()
    if not contexts:
        click.echo("Cannot find any context in kube-config file.")
        return

    click.echo(
        f"Current k8s context: {active_context['name']} on cluster {active_context['context']['cluster']}"
    )

    if namespace:
        echo_dict("Namespace info", get_namespace_info(namespace))
        return

    echo_table("Namespaces", get_namespaces())
