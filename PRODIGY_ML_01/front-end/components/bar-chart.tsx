
import { ResponsiveBar } from "@nivo/bar"

export default function Component({ prices }: { prices: number[] }) {
    return (
        <div className="w-full max-w-6xl p-4 mx-auto">
            <div className="pb-4">
                <h2 className="text-xl font-bold">Bar chart</h2>
                <p className="text-sm text-gray-500 dark:text-gray-400">Compare your sale Price with other Prices</p>
            </div>
            <div className="w-full h-[300px]">
                <BarChart prices={prices} />
            </div>
        </div>
    )
}

function BarChart({ prices }: { prices: number[] }) {
    const pricesWithId = prices.map((price, idx) => ({ id: idx, price: price }))

    return (
        <div className="w-full h-[300px]" >
            <ResponsiveBar
                data={pricesWithId}
                keys={["price"]}
                indexBy="id"
                margin={{ top: 0, right: 0, bottom: 40, left: 40 }}
                padding={0.3}
                colors={["#2563eb"]}
                axisBottom={{
                    tickSize: 0,
                    tickPadding: 16,
                }}
                axisLeft={{
                    tickSize: 0,
                    tickValues: 4,
                    tickPadding: 16,
                }}
                gridYValues={4}
                theme={{
                    tooltip: {
                        chip: {
                            borderRadius: "9999px",
                        },
                        container: {
                            fontSize: "12px",
                            textTransform: "capitalize",
                            borderRadius: "6px",
                        },
                    },
                    grid: {
                        line: {
                            stroke: "#f3f4f6",
                        },
                    },
                }}
                tooltipLabel={({ id }) => `${id}`}
                enableLabel={false}
                role="application"
                ariaLabel="A bar chart showing data"
            />
        </div>
    )
}
