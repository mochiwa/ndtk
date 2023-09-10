from nipyapi.nifi import ProcessGroupFlowEntity, ProcessGroupEntity, ProcessorEntity, RemoteProcessGroupEntity, \
    PortEntity, FunnelEntity

from app.flow.flow import Flow
from app.flow.node import Node


def mapping_flow(entity: ProcessGroupFlowEntity):
    def typeFactory(element):
        if isinstance(element, ProcessGroupEntity):
            return "PROCESS_GROUP"
        elif isinstance(element, ProcessorEntity):
            return "PROCESSOR"
        elif isinstance(element, RemoteProcessGroupEntity):
            return "REMOTE_PROCESS_GROUP"
        elif isinstance(element, PortEntity):
            return element.port_type
        elif isinstance(element, FunnelEntity):
            return "FUNNEL"

    def factory(data_list: []):
        if data_list is None:
            return []
        return [map_entity(e, typeFactory(e)) for e in data_list]

    process_groups = factory(entity.process_group_flow.flow.process_groups)
    remote_process_groups = factory(entity.process_group_flow.flow.remote_process_groups)
    processors = factory(entity.process_group_flow.flow.processors)
    input_ports = factory(entity.process_group_flow.flow.input_ports)
    output_ports = factory(entity.process_group_flow.flow.output_ports)
    funnels = factory(entity.process_group_flow.flow.funnels)
    return Flow(
        id=entity.process_group_flow.id,
        nodes=[*process_groups, *processors, *remote_process_groups, *input_ports, *output_ports, *funnels]
    )


def map_entity(entity, entity_type: str):
    return Node(
        id=entity.id,
        type=entity_type,
        x=entity.position.x,
        y=entity.position.y,
        name=getattr(entity.component,'name','') )
