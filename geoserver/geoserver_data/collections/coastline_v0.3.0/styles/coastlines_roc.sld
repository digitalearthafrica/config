<?xml version="1.0" encoding="UTF-8"?>
<sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" version="1.0.0">
    <sld:NamedLayer>
        <sld:Name>coastlines_v0.3.0 — rates_of_change</sld:Name>
        <sld:UserStyle>
            <sld:Name>coastlines_v0.3.0 — rates_of_change</sld:Name>
            <sld:FeatureTypeStyle>
                <sld:Name>name</sld:Name>
                <sld:Rule>
                    <sld:Name>Testing</sld:Name>
                    <sld:Title>Testing</sld:Title>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>-200</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>-2.5</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>-0.01</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>0.01</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                        </ogc:And>
                    </ogc:Filter>
                    <sld:MinScaleDenominator>5000.0</sld:MinScaleDenominator>
                    <sld:MaxScaleDenominator>500000.0</sld:MaxScaleDenominator>
                    <sld:PointSymbolizer>
                        <sld:Graphic>
                            <sld:Mark>
                                <sld:WellKnownName>circle</sld:WellKnownName>
                                <sld:Fill>
                                    <sld:CssParameter name="fill">#ca0020</sld:CssParameter>
                                </sld:Fill>
                                <sld:Stroke>
                                    <sld:CssParameter name="stroke">#ffffff</sld:CssParameter>
                                    <sld:CssParameter name="stroke-opacity">0</sld:CssParameter>
                                    <sld:CssParameter name="stroke-width">0.5</sld:CssParameter>
                                </sld:Stroke>
                            </sld:Mark>
                            <sld:Size>1</sld:Size>
                        </sld:Graphic>
                    </sld:PointSymbolizer>
                </sld:Rule>
                <sld:Rule>
                    <sld:Name>&lt; -2.50 m / year coastline retreat</sld:Name>
                    <sld:Title>&lt; -2.50 m / year coastline retreat</sld:Title>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>-200</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>-2.5</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>-0.01</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>0.01</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                        </ogc:And>
                    </ogc:Filter>
                    <sld:MinScaleDenominator>5000.0</sld:MinScaleDenominator>
                    <sld:MaxScaleDenominator>500000.0</sld:MaxScaleDenominator>
                    <sld:PointSymbolizer>
                        <sld:Graphic>
                            <sld:Mark>
                                <sld:WellKnownName>circle</sld:WellKnownName>
                                <sld:Fill>
                                    <sld:CssParameter name="fill">#ca0020</sld:CssParameter>
                                </sld:Fill>
                                <sld:Stroke>
                                    <sld:CssParameter name="stroke">#ffffff</sld:CssParameter>
                                    <sld:CssParameter name="stroke-opacity">0</sld:CssParameter>
                                    <sld:CssParameter name="stroke-width">0.5</sld:CssParameter>
                                </sld:Stroke>
                            </sld:Mark>
                            <sld:Size>10</sld:Size>
                        </sld:Graphic>
                    </sld:PointSymbolizer>
                </sld:Rule>
                <sld:Rule>
                    <sld:Name>-2.50 to -1.00 m / year</sld:Name>
                    <sld:Title>-2.50 to -1.00 m / year</sld:Title>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThan>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>-2.5</ogc:Literal>
                            </ogc:PropertyIsGreaterThan>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>-1</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>-0.01</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>0.01</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                        </ogc:And>
                    </ogc:Filter>
                    <sld:MinScaleDenominator>5000.0</sld:MinScaleDenominator>
                    <sld:MaxScaleDenominator>500000.0</sld:MaxScaleDenominator>
                    <sld:PointSymbolizer>
                        <sld:Graphic>
                            <sld:Mark>
                                <sld:WellKnownName>circle</sld:WellKnownName>
                                <sld:Fill>
                                    <sld:CssParameter name="fill">#da3c43</sld:CssParameter>
                                </sld:Fill>
                                <sld:Stroke>
                                    <sld:CssParameter name="stroke">#ffffff</sld:CssParameter>
                                    <sld:CssParameter name="stroke-opacity">0</sld:CssParameter>
                                    <sld:CssParameter name="stroke-width">0.5</sld:CssParameter>
                                </sld:Stroke>
                            </sld:Mark>
                            <sld:Size>9</sld:Size>
                        </sld:Graphic>
                    </sld:PointSymbolizer>
                </sld:Rule>
                <sld:Rule>
                    <sld:Name>-1.00 to -0.60 m / year</sld:Name>
                    <sld:Title>-1.00 to -0.60 m / year</sld:Title>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThan>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>-1</ogc:Literal>
                            </ogc:PropertyIsGreaterThan>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>-0.59999999999999998</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>-0.01</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>0.01</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                        </ogc:And>
                    </ogc:Filter>
                    <sld:MinScaleDenominator>5000.0</sld:MinScaleDenominator>
                    <sld:MaxScaleDenominator>500000.0</sld:MaxScaleDenominator>
                    <sld:PointSymbolizer>
                        <sld:Graphic>
                            <sld:Mark>
                                <sld:WellKnownName>circle</sld:WellKnownName>
                                <sld:Fill>
                                    <sld:CssParameter name="fill">#e97867</sld:CssParameter>
                                </sld:Fill>
                                <sld:Stroke>
                                    <sld:CssParameter name="stroke">#ffffff</sld:CssParameter>
                                    <sld:CssParameter name="stroke-opacity">0</sld:CssParameter>
                                    <sld:CssParameter name="stroke-width">0.5</sld:CssParameter>
                                </sld:Stroke>
                            </sld:Mark>
                            <sld:Size>7</sld:Size>
                        </sld:Graphic>
                    </sld:PointSymbolizer>
                </sld:Rule>
                <sld:Rule>
                    <sld:Name>-0.60 to -0.30 m / year</sld:Name>
                    <sld:Title>-0.60 to -0.30 m / year</sld:Title>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThan>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>-0.59999999999999998</ogc:Literal>
                            </ogc:PropertyIsGreaterThan>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>-0.29999999999999999</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>-0.01</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>0.01</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                        </ogc:And>
                    </ogc:Filter>
                    <sld:MinScaleDenominator>5000.0</sld:MinScaleDenominator>
                    <sld:MaxScaleDenominator>500000.0</sld:MaxScaleDenominator>
                    <sld:PointSymbolizer>
                        <sld:Graphic>
                            <sld:Mark>
                                <sld:WellKnownName>circle</sld:WellKnownName>
                                <sld:Fill>
                                    <sld:CssParameter name="fill">#f5ad8d</sld:CssParameter>
                                </sld:Fill>
                                <sld:Stroke>
                                    <sld:CssParameter name="stroke">#ffffff</sld:CssParameter>
                                    <sld:CssParameter name="stroke-opacity">0</sld:CssParameter>
                                    <sld:CssParameter name="stroke-width">0.5</sld:CssParameter>
                                </sld:Stroke>
                            </sld:Mark>
                            <sld:Size>6</sld:Size>
                        </sld:Graphic>
                    </sld:PointSymbolizer>
                </sld:Rule>
                <sld:Rule>
                    <sld:Name>-0.30 to -0.10 m / year</sld:Name>
                    <sld:Title>-0.30 to -0.10 m / year</sld:Title>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThan>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>-0.29999999999999999</ogc:Literal>
                            </ogc:PropertyIsGreaterThan>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>-0.10000000000000001</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>-0.01</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>0.01</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                        </ogc:And>
                    </ogc:Filter>
                    <sld:MinScaleDenominator>5000.0</sld:MinScaleDenominator>
                    <sld:MaxScaleDenominator>500000.0</sld:MaxScaleDenominator>
                    <sld:PointSymbolizer>
                        <sld:Graphic>
                            <sld:Mark>
                                <sld:WellKnownName>circle</sld:WellKnownName>
                                <sld:Fill>
                                    <sld:CssParameter name="fill">#f6cbb7</sld:CssParameter>
                                </sld:Fill>
                                <sld:Stroke>
                                    <sld:CssParameter name="stroke">#ffffff</sld:CssParameter>
                                    <sld:CssParameter name="stroke-opacity">0</sld:CssParameter>
                                    <sld:CssParameter name="stroke-width">0.5</sld:CssParameter>
                                </sld:Stroke>
                            </sld:Mark>
                            <sld:Size>5</sld:Size>
                        </sld:Graphic>
                    </sld:PointSymbolizer>
                </sld:Rule>
                <sld:Rule>
                    <sld:Name>-0.10 to 0.00 m / year</sld:Name>
                    <sld:Title>-0.10 to 0.00 m / year</sld:Title>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThan>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>-0.10000000000000001</ogc:Literal>
                            </ogc:PropertyIsGreaterThan>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>0</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>-0.01</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>0.01</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                        </ogc:And>
                    </ogc:Filter>
                    <sld:MinScaleDenominator>5000.0</sld:MinScaleDenominator>
                    <sld:MaxScaleDenominator>500000.0</sld:MaxScaleDenominator>
                    <sld:PointSymbolizer>
                        <sld:Graphic>
                            <sld:Mark>
                                <sld:WellKnownName>circle</sld:WellKnownName>
                                <sld:Fill>
                                    <sld:CssParameter name="fill">#f7e8e2</sld:CssParameter>
                                </sld:Fill>
                                <sld:Stroke>
                                    <sld:CssParameter name="stroke">#ffffff</sld:CssParameter>
                                    <sld:CssParameter name="stroke-opacity">0</sld:CssParameter>
                                    <sld:CssParameter name="stroke-width">0.5</sld:CssParameter>
                                </sld:Stroke>
                            </sld:Mark>
                            <sld:Size>4</sld:Size>
                        </sld:Graphic>
                    </sld:PointSymbolizer>
                </sld:Rule>
                <sld:Rule>
                    <sld:Name>0.00 to 0.10 m / year</sld:Name>
                    <sld:Title>0.00 to 0.10 m / year</sld:Title>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThan>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>0</ogc:Literal>
                            </ogc:PropertyIsGreaterThan>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>0.10000000000000001</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>-0.01</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>0.01</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                        </ogc:And>
                    </ogc:Filter>
                    <sld:MinScaleDenominator>5000.0</sld:MinScaleDenominator>
                    <sld:MaxScaleDenominator>500000.0</sld:MaxScaleDenominator>
                    <sld:PointSymbolizer>
                        <sld:Graphic>
                            <sld:Mark>
                                <sld:WellKnownName>circle</sld:WellKnownName>
                                <sld:Fill>
                                    <sld:CssParameter name="fill">#e5eef3</sld:CssParameter>
                                </sld:Fill>
                                <sld:Stroke>
                                    <sld:CssParameter name="stroke">#ffffff</sld:CssParameter>
                                    <sld:CssParameter name="stroke-opacity">0</sld:CssParameter>
                                    <sld:CssParameter name="stroke-width">0.5</sld:CssParameter>
                                </sld:Stroke>
                            </sld:Mark>
                            <sld:Size>4</sld:Size>
                        </sld:Graphic>
                    </sld:PointSymbolizer>
                </sld:Rule>
                <sld:Rule>
                    <sld:Name>0.10 to 0.30 m / year</sld:Name>
                    <sld:Title>0.10 to 0.30 m / year</sld:Title>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThan>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>0.10000000000000001</ogc:Literal>
                            </ogc:PropertyIsGreaterThan>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>0.29999999999999999</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>-0.01</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>0.01</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                        </ogc:And>
                    </ogc:Filter>
                    <sld:MinScaleDenominator>5000.0</sld:MinScaleDenominator>
                    <sld:MaxScaleDenominator>500000.0</sld:MaxScaleDenominator>
                    <sld:PointSymbolizer>
                        <sld:Graphic>
                            <sld:Mark>
                                <sld:WellKnownName>circle</sld:WellKnownName>
                                <sld:Fill>
                                    <sld:CssParameter name="fill">#c0dcea</sld:CssParameter>
                                </sld:Fill>
                                <sld:Stroke>
                                    <sld:CssParameter name="stroke">#ffffff</sld:CssParameter>
                                    <sld:CssParameter name="stroke-opacity">0</sld:CssParameter>
                                    <sld:CssParameter name="stroke-width">0.5</sld:CssParameter>
                                </sld:Stroke>
                            </sld:Mark>
                            <sld:Size>5</sld:Size>
                        </sld:Graphic>
                    </sld:PointSymbolizer>
                </sld:Rule>
                <sld:Rule>
                    <sld:Name>0.30 to 0.60 m / year</sld:Name>
                    <sld:Title>0.30 to 0.60 m / year</sld:Title>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThan>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>0.29999999999999999</ogc:Literal>
                            </ogc:PropertyIsGreaterThan>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>0.59999999999999998</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>-0.01</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>0.01</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                        </ogc:And>
                    </ogc:Filter>
                    <sld:MinScaleDenominator>5000.0</sld:MinScaleDenominator>
                    <sld:MaxScaleDenominator>500000.0</sld:MaxScaleDenominator>
                    <sld:PointSymbolizer>
                        <sld:Graphic>
                            <sld:Mark>
                                <sld:WellKnownName>circle</sld:WellKnownName>
                                <sld:Fill>
                                    <sld:CssParameter name="fill">#9bcae1</sld:CssParameter>
                                </sld:Fill>
                                <sld:Stroke>
                                    <sld:CssParameter name="stroke">#ffffff</sld:CssParameter>
                                    <sld:CssParameter name="stroke-opacity">0</sld:CssParameter>
                                    <sld:CssParameter name="stroke-width">0.5</sld:CssParameter>
                                </sld:Stroke>
                            </sld:Mark>
                            <sld:Size>6</sld:Size>
                        </sld:Graphic>
                    </sld:PointSymbolizer>
                </sld:Rule>
                <sld:Rule>
                    <sld:Name>0.60 to 1.00 m / year</sld:Name>
                    <sld:Title>0.60 to 1.00 m / year</sld:Title>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThan>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>0.59999999999999998</ogc:Literal>
                            </ogc:PropertyIsGreaterThan>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>1</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>-0.01</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>0.01</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                        </ogc:And>
                    </ogc:Filter>
                    <sld:MinScaleDenominator>5000.0</sld:MinScaleDenominator>
                    <sld:MaxScaleDenominator>500000.0</sld:MaxScaleDenominator>
                    <sld:PointSymbolizer>
                        <sld:Graphic>
                            <sld:Mark>
                                <sld:WellKnownName>circle</sld:WellKnownName>
                                <sld:Fill>
                                    <sld:CssParameter name="fill">#6baed2</sld:CssParameter>
                                </sld:Fill>
                                <sld:Stroke>
                                    <sld:CssParameter name="stroke">#ffffff</sld:CssParameter>
                                    <sld:CssParameter name="stroke-opacity">0</sld:CssParameter>
                                    <sld:CssParameter name="stroke-width">0.5</sld:CssParameter>
                                </sld:Stroke>
                            </sld:Mark>
                            <sld:Size>7</sld:Size>
                        </sld:Graphic>
                    </sld:PointSymbolizer>
                </sld:Rule>
                <sld:Rule>
                    <sld:Name>1.00 to 2.50 m / year</sld:Name>
                    <sld:Title>1.00 to 2.50 m / year</sld:Title>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThan>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>1</ogc:Literal>
                            </ogc:PropertyIsGreaterThan>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>2.5</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>-0.01</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>0.01</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                        </ogc:And>
                    </ogc:Filter>
                    <sld:MinScaleDenominator>5000.0</sld:MinScaleDenominator>
                    <sld:MaxScaleDenominator>500000.0</sld:MaxScaleDenominator>
                    <sld:PointSymbolizer>
                        <sld:Graphic>
                            <sld:Mark>
                                <sld:WellKnownName>circle</sld:WellKnownName>
                                <sld:Fill>
                                    <sld:CssParameter name="fill">#3890c1</sld:CssParameter>
                                </sld:Fill>
                                <sld:Stroke>
                                    <sld:CssParameter name="stroke">#ffffff</sld:CssParameter>
                                    <sld:CssParameter name="stroke-opacity">0</sld:CssParameter>
                                    <sld:CssParameter name="stroke-width">0.5</sld:CssParameter>
                                </sld:Stroke>
                            </sld:Mark>
                            <sld:Size>9</sld:Size>
                        </sld:Graphic>
                    </sld:PointSymbolizer>
                </sld:Rule>
                <sld:Rule>
                    <sld:Name>&gt; 2.50 m / year coastline growth</sld:Name>
                    <sld:Title>&gt; 2.50 m / year coastline growth</sld:Title>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:PropertyIsGreaterThan>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>2.5</ogc:Literal>
                            </ogc:PropertyIsGreaterThan>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                                <ogc:Literal>200</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                            <ogc:PropertyIsGreaterThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>-0.01</ogc:Literal>
                            </ogc:PropertyIsGreaterThanOrEqualTo>
                            <ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:PropertyName>sig_time</ogc:PropertyName>
                                <ogc:Literal>0.01</ogc:Literal>
                            </ogc:PropertyIsLessThanOrEqualTo>
                        </ogc:And>
                    </ogc:Filter>
                    <sld:MinScaleDenominator>5000.0</sld:MinScaleDenominator>
                    <sld:MaxScaleDenominator>500000.0</sld:MaxScaleDenominator>
                    <sld:PointSymbolizer>
                        <sld:Graphic>
                            <sld:Mark>
                                <sld:WellKnownName>circle</sld:WellKnownName>
                                <sld:Fill>
                                    <sld:CssParameter name="fill">#0571b0</sld:CssParameter>
                                </sld:Fill>
                                <sld:Stroke>
                                    <sld:CssParameter name="stroke">#ffffff</sld:CssParameter>
                                    <sld:CssParameter name="stroke-opacity">0</sld:CssParameter>
                                    <sld:CssParameter name="stroke-width">0.5</sld:CssParameter>
                                </sld:Stroke>
                            </sld:Mark>
                            <sld:Size>10</sld:Size>
                        </sld:Graphic>
                    </sld:PointSymbolizer>
                </sld:Rule>
                <sld:Rule>
                    <ogc:Filter>
                        <ogc:And>
                            <ogc:And>
                                <ogc:PropertyIsLessThanOrEqualTo>
                                    <ogc:PropertyName>sig_time</ogc:PropertyName>
                                    <ogc:Literal>0.01</ogc:Literal>
                                </ogc:PropertyIsLessThanOrEqualTo>
                                <ogc:Or>
                                    <ogc:PropertyIsGreaterThanOrEqualTo>
                                        <ogc:PropertyName>rate_time</ogc:PropertyName>
                                        <ogc:Literal>0.3</ogc:Literal>
                                    </ogc:PropertyIsGreaterThanOrEqualTo>
                                    <ogc:PropertyIsLessThanOrEqualTo>
                                        <ogc:PropertyName>rate_time</ogc:PropertyName>
                                        <ogc:Literal>-0.3</ogc:Literal>
                                    </ogc:PropertyIsLessThanOrEqualTo>
                                </ogc:Or>
                            </ogc:And>
                            <ogc:PropertyIsGreaterThan>
                                <ogc:PropertyName>valid_obs</ogc:PropertyName>
                                <ogc:Literal>10</ogc:Literal>
                            </ogc:PropertyIsGreaterThan>
                        </ogc:And>
                    </ogc:Filter>
                    <sld:MinScaleDenominator>5000.0</sld:MinScaleDenominator>
                    <sld:MaxScaleDenominator>500000.0</sld:MaxScaleDenominator>
                    <sld:TextSymbolizer>
                        <sld:Label>
                            <ogc:Function name="numberFormat">
                                <ogc:Literal>0.0</ogc:Literal>
                                <ogc:PropertyName>rate_time</ogc:PropertyName>
                            </ogc:Function>
                            <![CDATA[ m (±]]>
                            <ogc:Function name="numberFormat">
                                <ogc:Literal>0.0</ogc:Literal>
                                <ogc:Mul>
                                    <ogc:PropertyName>se_time</ogc:PropertyName>
                                    <ogc:Literal>1.96</ogc:Literal>
                                </ogc:Mul>
                            </ogc:Function>)
                        </sld:Label>
                        <sld:Font>
                            <sld:CssParameter name="font-family">SansSerif.plain</sld:CssParameter>
                            <sld:CssParameter name="font-size">10</sld:CssParameter>
                            <sld:CssParameter name="font-style">normal</sld:CssParameter>
                            <sld:CssParameter name="font-weight">normal</sld:CssParameter>
                        </sld:Font>
                        <sld:LabelPlacement>
                            <sld:PointPlacement>
                                <sld:AnchorPoint>
                                    <sld:AnchorPointX>1</sld:AnchorPointX>
                                    <sld:AnchorPointY>0.5</sld:AnchorPointY>
                                </sld:AnchorPoint>
                                <sld:Displacement>
                                    <sld:DisplacementX>-12</sld:DisplacementX>
                                    <sld:DisplacementY>0</sld:DisplacementY>
                                </sld:Displacement>
                            </sld:PointPlacement>
                        </sld:LabelPlacement>
                        <sld:Halo>
                            <sld:Radius>1.5</sld:Radius>
                            <sld:Fill>
                                <sld:CssParameter name="fill">#000000</sld:CssParameter>
                                <sld:CssParameter name="fill-opacity">0.5</sld:CssParameter>
                            </sld:Fill>
                        </sld:Halo>
                        <sld:Fill>
                            <sld:CssParameter name="fill">#ffffff</sld:CssParameter>
                        </sld:Fill>
                        <sld:Priority>100</sld:Priority>
                    </sld:TextSymbolizer>
                </sld:Rule>
                <sld:VendorOption name="sortBy">rate_time</sld:VendorOption>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:NamedLayer>
</sld:StyledLayerDescriptor>
