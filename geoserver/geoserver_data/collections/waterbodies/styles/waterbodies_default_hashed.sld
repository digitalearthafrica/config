<?xml version='1.0' encoding='UTF-8'?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:gml="http://www.opengis.net/gml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd" version="1.0.0">
    <NamedLayer>
        <Name>waterbodies</Name>
        <UserStyle>
            <Name>waterbodies</Name>
            <FeatureTypeStyle>
                <Rule>
                    <Name>Historical Extent</Name>
                    <PolygonSymbolizer>
                        <Fill>
                            <GraphicFill>
                                <Graphic>
                                    <Mark>
                                        <WellKnownName>shape://times</WellKnownName>
                                        <Stroke>
                                            <CssParameter name="stroke">#23d9f1</CssParameter>
                                            <CssParameter name="stroke-opacity">1</CssParameter>
                                        </Stroke>
                                    </Mark>
                                </Graphic>
                            </GraphicFill>
                        </Fill>
                        <Stroke>
                            <CssParameter name="stroke">#23d9f1</CssParameter>
                            <CssParameter name="stroke-opacity">1</CssParameter>
                            <CssParameter name="stroke-width">1</CssParameter>
                            <CssParameter name="stroke-linejoin">bevel</CssParameter>
                        </Stroke>
                    </PolygonSymbolizer>
                </Rule>
            </FeatureTypeStyle>
        </UserStyle>
    </NamedLayer>
</StyledLayerDescriptor>
