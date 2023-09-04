from integration.abstract_integration_test import TestAbstractIntegration


class TestItGetFlow(TestAbstractIntegration):

    def test_get_flow_should_return_error_project_not_found_when_project_not_found(self):
        response = self.client.get("/nifi/uuid/flow/root")

        self._assert_error(response, 404, 'NOT_FOUND', "Project uuid not found.")

    def test_get_flow_should_return_error_flow_not_found_when_flow_not_found(self):
        response = self.client.get(f"/nifi/{self.project.project_id}/flow/root")

        self._assert_error(response, 404, 'NOT_FOUND', "Flow 'root' not found.")


    def test_get_flow_should_return_the_flow_found(self):
        response = self.client.get("/nifi/uuid/flow/root")

        assert response.status_code is 200
        value = response.json()

        assert value['id'] == ''
        assert len(value['nodes']) == 3
        assert value['nodes'][0]['id'] == 'processor_id'
        assert value['nodes'][0]['x'] == '100'
        assert value['nodes'][0]['y'] == '100'
        assert value['nodes'][0]['type'] == 'processor'

        assert value['nodes'][1]['id'] == 'group_id'
        assert value['nodes'][1]['x'] == '100'
        assert value['nodes'][1]['y'] == '100'
        assert value['nodes'][1]['type'] == 'process_group'

        assert value['nodes'][2]['id'] == 'input_port_id'
        assert value['nodes'][2]['x'] == '100'
        assert value['nodes'][2]['y'] == '100'
        assert value['nodes'][2]['type'] == 'input_port'

        assert value['nodes'][3]['id'] == 'output_port_id'
        assert value['nodes'][3]['x'] == '100'
        assert value['nodes'][3]['y'] == '100'
        assert value['nodes'][3]['type'] == 'output_port'




