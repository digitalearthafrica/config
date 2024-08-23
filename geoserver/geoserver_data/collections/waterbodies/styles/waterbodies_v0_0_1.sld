<?xml version="1.0" encoding="UTF-8"?>
<sld:StyledLayerDescriptor xmlns:sld="http://www.opengis.net/sld" xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" version="1.1.0">
    <sld:NamedLayer>
        <sld:Name>waterbodies_v0_0_1</sld:Name>
        <sld:UserStyle>
            <sld:Name>waterbodies_v0_0_1</sld:Name>
            <sld:FeatureTypeStyle>
                <sld:Name>name</sld:Name>
                <sld:Rule>
                    <sld:Name>Water body</sld:Name>
                    <sld:PolygonSymbolizer>
                        <sld:Fill>
                            <sld:GraphicFill>
                                <sld:Graphic>
                                    <sld:ExternalGraphic>
                                        <sld:OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="file:/opt/geoserver/data_dir/workspaces/waterbodies1/styles/deafrica_waterbodies_singlehash.png"/>
                                        <sld:Format>image/png</sld:Format>
                                    </sld:ExternalGraphic>
                                    <sld:Size>9</sld:Size>
                                </sld:Graphic>
                            </sld:GraphicFill>
                        </sld:Fill>
                    </sld:PolygonSymbolizer>
                    <sld:LineSymbolizer>
                        <sld:Stroke>
                            <sld:CssParameter name="stroke">#11ccff</sld:CssParameter>
                            <sld:CssParameter name="stroke-linecap">square</sld:CssParameter>
                            <sld:CssParameter name="stroke-linejoin">bevel</sld:CssParameter>
                            <sld:CssParameter name="stroke-width">2</sld:CssParameter>
                        </sld:Stroke>
                    </sld:LineSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:NamedLayer>
</sld:StyledLayerDescriptor>