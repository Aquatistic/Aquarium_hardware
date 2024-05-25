from effectors.EffectorService import EffectorService
from typing import List
import json
import sseclient
import urllib3


class EffectorBackendInteractors:
    def __init__(self, backend_destination: str, effectors: List[EffectorService]):
        self._backend_destination = backend_destination
        self._effectors = effectors
        self._sse_clinet = sseclient.SSEClient(self._open_stream())
        
    def _open_stream(self):
        http = urllib3.PoolManager()
        return http.request('GET', self._backend_destination, preload_content=False)
    
    def run(self):
        server_event_stream = self._sse_clinet.events()
        while True:
            effector_control_event = json.loads(next(server_event_stream).data)
            print(effector_control_event)
            try:
                for effector in self._effectors:
                    print(type(effector))
                    if effector.get_effector_id() == int(effector_control_event["effectorId"]):
                        effector.send_controll_to_effector(effector_control_event)
                        break
                
            except:
                pass
            
