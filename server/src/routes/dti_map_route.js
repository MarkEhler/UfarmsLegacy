import express from 'express'
import ash from 'express-async-handler'
import dayjs from 'dayjs';

const app = express()
export {app}
import {dice_pool} from '../../utils/dice_pool.js'
//import { auth } from "../../middleware/auth.js";




app.get(
  "/hazardsAndCategories",
  ash(async (req, res) => {
//     const sql1 = `select * from ethel_data_category order by category_name`;
//     const result1 = await dice_pool.query(sql1)

//     const sql2 = `select * from ethel_hazard order by hazard_name`;
//     const result2 = await dice_pool.query(sql2)

//     const sql3 = `select * from ethel_data_category c
// inner join ethel_datasource_to_category dtc on dtc.category_id = c.id
// inner join ethel_hazard_to_datasource htd on htd.datasource_id = dtc.datasource_id
// inner join ethel_hazard h on htd.hazard_id = h.id;
// `
//     const result3 = await dice_pool.query(sql3)

    const sql4 = `SELECT
ed.id as datasource_id,
ed.datasource_name as datasource_name,
import_to_azure,
eh.id as hazard_id,
hazard_name,
hazard_color,
hazard_attribute_name,
edc.id as category_id,
category_name,
category_color,
url
FROM
ethel_datasource ed
full OUTER JOIN ethel_hazard_to_datasource ehtd ON ehtd.datasource_id = ed.id
full OUTER JOIN ethel_hazard eh ON eh.id = ehtd.hazard_id
full OUTER JOIN ethel_datasource_attributes eda ON eda.datasource_id = ed.id
full OUTER JOIN ethel_hazard_to_data_category ehtdc ON ehtd.hazard_id = ehtdc.hazard_id
full outer join ethel_data_category edc on edc.id = ehtdc.category_id where ed.id is not null and ed.is_etl_active = true and ed.is_dynamic = true and ed.is_private_data = false;`
  const result4 = await dice_pool.query(sql4)

    res.send(result4.rows);
  })
);

app.get(
  "/ethelData",
  ash(async (req, res) => {
    const sql = `select 
    r.dataset_id,
    r.datasource_id,
    r.feature_id,
    r.feature_name,
    r.last_modified,
    r.last_updated_at,
    r.properties,
    ST_AsGeoJSON(r.geometry) AS geojson
    from ethel_latest_run r
    ORDER BY r.feature_name
    `;
    const result = await dice_pool.query(sql)



    res.send(result.rows.map(r=>{
      return {
        ...r,
        geojson: JSON.parse(r.geojson)
      }
    }))
  })
);

app.get(
  "/models",
  ash(async (req, res) => {

    let sql;
    let result
    let forecastEndDatetime = dayjs(req.query.selected_datetime).add(5,"day").format("YYYY-MM-DD HH:mm:ss")

    if(req.query.model_code === "ERI")
    {
      sql = `SELECT 
        b.globalid AS boundary_id,
        b.state_name,
        b.county_name,
        b.political_boundaries_type,
        eri.id AS eri_feature_id,
        eri.max_wind,
        eri.eri,
        eri.timestamp,
        eri.model_runtime
      FROM legal_entity_boundaries b
      INNER JOIN energy_reliability_index eri ON eri.globalid = b.globalid
      WHERE b.globalid = '${req.query.boundary_id}'
      AND b.political_boundaries_type = '${req.query.political_boundaries_type}'

      AND eri.timestamp >= to_timestamp('${req.query.selected_datetime}','YYYY-MM-DD HH24:MI:SS')
      AND eri.timestamp < to_timestamp('${forecastEndDatetime}','YYYY-MM-DD HH24:MI:SS')

      ORDER BY eri.timestamp asc
      `
    }
    
    result = await dice_pool.query(sql)

    res.send(result.rows)
  })
);

// TODO authorize - not just authenticate - group membership + RBAC (+ subscription)


