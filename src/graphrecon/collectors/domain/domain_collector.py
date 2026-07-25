from graphrecon.models.domain import DomainModel
from graphrecon.models.resource import ResourceModel


class DomainCollector:
    """
    Groups resources by domain.
    """

    def collect(
        self,
        resources: list[ResourceModel],
    ) -> list[DomainModel]:

        grouped: dict[str, list[ResourceModel]] = {}

        for resource in resources:
            grouped.setdefault(resource.domain, []).append(resource)

        domains: list[DomainModel] = []

        for domain, items in sorted(grouped.items()):

            domains.append(
                DomainModel(
                    domain=domain,
                    resource_count=len(items),
                    third_party=items[0].third_party,
                )
            )

        return domains
