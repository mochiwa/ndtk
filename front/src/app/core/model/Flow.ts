export interface Flow {
  flow_id: string,
  nodes: Node[],
}

export interface Node{
  "id": string,
  "x": number,
  "y": number,
  "type": string
}


export interface  GetFlowRequest{
  'project_id': string,
  'flow_id': string
}
