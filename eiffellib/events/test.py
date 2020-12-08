import uuid

import eiffel_artifact_created_event as artc

ev = artc.EiffelArtifactCreatedEvent(
    data=artc.EiffelArtifactCreatedData(identity="pkg:foo/bar"),
    links=[
        artc.EiffelLink(type="ARTIFACT", target=uuid.uuid4()),
        artc.EiffelLink(type="FLOW_CONTEXT", target=uuid.uuid4()),
    ],
)
print(ev.json(exclude_defaults=True))
