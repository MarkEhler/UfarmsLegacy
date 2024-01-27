// export const users = mysqlTable('Users', {
//     id: serial('id').primaryKey(),
//     username: varchar('username', { length: 120 }),
//     tagline: varchar('tagline', { length: 250 }),
//     display_name: varchar('display_name', { length: 250 }),
//     img_url: varchar('img_url', { length: 500 })
//   })
  
//   export const blocks = mysqlTable('Ufarms', {
//     id: serial('id').primaryKey(),
//     url: varchar('url', { length: 200 }),
//     block_type: int('type'),
//     // 👇 The following line will create a foreign key constraint
//     user_id: int('user_id').references(() => users.id),
//     label: varchar('label', { length: 200 })
//   })