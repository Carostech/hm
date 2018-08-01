USE  hotels;

-- Getting all booking made yesterday and today as new arrivals
CREATE VIEW ArrivalsView AS
	SELECT
		booking_id AS booking_id,
    hotelweb_booking.user_id AS user_id,
		hotel_id AS hotel_id,
		hotelweb_packages.package_id AS package_id,
    facility_id AS facility_id,
    hotelweb_users.name AS full_name,
    hotelweb_rooms.room_number,
    hotelweb_rooms.room_type AS room_type,
    hotelweb_packages.package_name,
    hotelweb_booking.status AS status,
    confirmation_number AS confirmation_number
  FROM
    hotelweb_booking
  INNER JOIN hotelweb_users
    ON hotelweb_users.user_id=hotelweb_booking.user_id
	INNER JOIN hotelweb_packages
		ON hotelweb_booking.package_id=hotelweb_packages.package_id
	INNER JOIN hotelweb_rooms
		ON hotelweb_booking.facility_id=hotelweb_rooms.room_id
    AND hotelweb_booking.facility_type='room'
	WHERE hotelweb_booking.start_date = CURDATE() - INTERVAL 1 DAY
		OR hotelweb_booking.start_date= CURDATE() 
	ORDER BY hotelweb_booking.created_on;
    
-- Getting all departures yesterday and today 
CREATE VIEW DeparturesView AS
	SELECT
		booking_id AS booking_id,
    hotelweb_booking.user_id AS user_id,
		hotel_id AS hotel_id,
		hotelweb_packages.package_id AS package_id,
    facility_id AS facility_id,
    hotelweb_users.name AS full_name,
    hotelweb_rooms.room_number,
    hotelweb_rooms.room_type AS room_type,
    hotelweb_packages.package_name,
    hotelweb_booking.status AS status,
    confirmation_number AS confirmation_number
  FROM
		hotelweb_booking
  INNER JOIN hotelweb_users
    ON hotelweb_users.user_id=hotelweb_booking.user_id
	INNER JOIN hotelweb_packages
		ON hotelweb_booking.package_id=hotelweb_packages.package_id
	INNER JOIN hotelweb_rooms
		ON hotelweb_booking.facility_id=hotelweb_rooms.room_id
    AND hotelweb_booking.facility_type='room'
	WHERE hotelweb_booking.end_date = CURDATE() - INTERVAL 1 DAY
		OR hotelweb_booking.end_date= CURDATE() 
	ORDER BY hotelweb_booking.created_on;
 
 -- Summary of total bookings (arrivals and departures and rooms occupied)
 CREATE VIEW BookingSummaryView AS
	SELECT
		(
			SELECT
				COUNT(start_date) AS total_arrival
			FROM hotelweb_booking
			WHERE hotelweb_booking.start_date =CURDATE()
				AND hotelweb_booking.facility_type='room'
		) AS total_arrivals,
		(
			SELECT
				COUNT(start_date) AS total_departures
			FROM hotelweb_booking
			WHERE hotelweb_booking.end_date =CURDATE()
				AND hotelweb_booking.facility_type='room'
		) AS total_departures,
		(
			SELECT
				COUNT(*) AS rooms_occupied
			FROM hotelweb_booking
				WHERE hotelweb_booking.end_date >= CURDATE()
					AND hotelweb_booking.facility_type='room'
		) AS rooms_occupied;

-- Getting booking summary of today
CREATE VIEW TodayBookingView AS
	SELECT
		(
			SELECT
				COUNT(created_on) AS booked_today
			FROM hotelweb_booking
			WHERE hotelweb_booking.created_on =CURDATE()
				AND hotelweb_booking.facility_type='room'
		) AS total_booked_today,
		(
			SELECT
				SUM(end_date-start_date) AS nights
			FROM hotelweb_booking
			WHERE hotelweb_booking.end_date >=CURDATE()
				AND hotelweb_booking.facility_type='room'
		) AS total_nights,
        (
			SELECT
				COUNT(booking_id)
			FROM hotelweb_booking
			WHERE hotelweb_booking.booking_date=CURDATE()
				AND hotelweb_booking.facility_type='room'
                AND hotelweb_booking.status='cancelled'
		) AS total_cancellations,
        (
			SELECT
				COUNT(booking_id) AS total_overbooking
			FROM hotelweb_booking
			WHERE hotelweb_booking.booking_date=CURDATE()
				AND hotelweb_booking.facility_type='room'
                HAVING (count(booking_id) > (SELECT COUNT(*) FROM hotelweb_rooms))
		) AS total_overbooking;
        
-- Getting cancellation records and people who cancelled them
CREATE VIEW CancellationView AS
	SELECT
    booking_id AS booking_id,
    hotelweb_booking.user_id AS user_id,
		hotel_id AS hotel_id,
		hotelweb_packages.package_id AS package_id,
    facility_id AS facility_id,
    hotelweb_users.name AS full_name,
    hotelweb_rooms.room_number,
    hotelweb_rooms.room_type AS room_type,
    hotelweb_booking.booking_date,
    hotelweb_packages.package_name
	FROM hotelweb_booking
    INNER JOIN hotelweb_users 
    ON hotelweb_users.user_id=hotelweb_booking.user_id
	INNER JOIN hotelweb_packages
		ON hotelweb_booking.package_id=hotelweb_packages.package_id
	INNER JOIN hotelweb_rooms
		ON hotelweb_booking.facility_id=hotelweb_rooms.room_id
	WHERE hotelweb_booking.booking_date=CURDATE()
		AND hotelweb_booking.facility_type='room'
		AND hotelweb_booking.status='cancelled' ; 
 
-- Getting overbookings
CREATE VIEW OverBookingsView AS
	SELECT
    booking_id AS booking_id,
    hotelweb_booking.user_id AS user_id,
		hotel_id AS hotel_id,
		hotelweb_packages.package_id AS package_id,
    facility_id AS facility_id,
    hotelweb_users.name AS full_name,
    hotelweb_rooms.room_number,
    hotelweb_rooms.room_type AS room_type,
    hotelweb_packages.package_name
	FROM hotelweb_booking
    INNER JOIN hotelweb_users 
    ON hotelweb_users.user_id=hotelweb_booking.user_id
	INNER JOIN hotelweb_packages
	  ON hotelweb_booking.package_id=hotelweb_packages.package_id
	INNER JOIN hotelweb_rooms
	  ON hotelweb_booking.facility_id=hotelweb_rooms.room_id
	WHERE hotelweb_booking.booking_date=CURDATE()
    AND hotelweb_booking.facility_type='room'
    HAVING (count(booking_id) > (SELECT COUNT(*) FROM hotelweb_rooms));
	
	
-- Getting rooms occupied and people occupying them
CREATE VIEW RoomsOccupiedView AS
	SELECT
    booking_id AS booking_id,
    hotelweb_booking.user_id AS user_id,
		hotel_id AS hotel_id,
		hotelweb_packages.package_id AS package_id,
    facility_id AS facility_id,
    hotelweb_users.name AS full_name,
    hotelweb_rooms.room_number,
    hotelweb_rooms.room_type AS room_type,
    hotelweb_booking.booking_date,
    hotelweb_packages.package_name
	FROM hotelweb_booking
    INNER JOIN hotelweb_users 
    ON hotelweb_users.user_id=hotelweb_booking.user_id
	INNER JOIN hotelweb_packages
		ON hotelweb_booking.package_id=hotelweb_packages.package_id
	INNER JOIN hotelweb_rooms
		ON hotelweb_booking.facility_id=hotelweb_rooms.room_id
	WHERE hotelweb_booking.end_date >= CURDATE()
    AND hotelweb_booking.facility_type='room';
     
-- Getting guests
CREATE VIEW InhouseGuestsView AS
	SELECT 
		guest_id AS guest_id,
		name AS name,
		phone AS phone,
		id_number AS id_number,
		created_on AS created_on
	FROM hotelweb_guests;
  
-- Tracking trends most used facilities
CREATE VIEW MostUsedFacilityView AS
	SELECT 
		COUNT(utm.tracking_id) AS usage_count,
        utm.facility_id AS  facility_id,
        hf.facility_name AS facility
	FROM
		hotelweb_usertrackingmovements AS utm
  LEFT JOIN hotelweb_facilities AS hf
		ON utm.facility_id=hf.facility_id
  ORDER BY usage_count DESC
  LIMIT 3;

-- Tracking trends least used facilities
CREATE VIEW LeastUsedFacilityView AS
	SELECT
		COUNT(utm.tracking_id) AS usage_count,
        utm.facility_id AS  facility_id,
        hf.facility_name AS facility
	FROM
		hotelweb_usertrackingmovements AS utm
  LEFT JOIN hotelweb_facilities AS hf
		ON utm.facility_id=hf.facility_id
  ORDER BY usage_count ASC
  LIMIT 3;

    -- Cleaning room list view
  CREATE VIEW cleaningRoomView AS
	SELECT
		hc.facility_id AS facility_id,
    hc.facility_type AS  facility_type_id,
    hr.room_number AS room_number,
    hc.status AS status,
    hc.worker_id AS worker_id,
    hw.name AS worker_name,
    hc.created_by AS created_by,
    hc.created_on AS created_on
	FROM
		hotelweb_cleaning AS hc
    INNER JOIN hotelweb_workers AS hw
			ON hc.worker_id=hw.worker_id
		INNER JOIN hotelweb_rooms AS hr
			ON hr.room_id=hc.facility_id;

-- Cleaning facility list view
  CREATE VIEW cleaningFacilityView AS
	SELECT
		hc.facility_id AS facility_id,
    hc.facility_type AS  facility_type_id,
    hf.facility_number AS facility_number,
    hc.status AS status,
    hc.worker_id AS worker_id,
    hw.name AS worker_name,
    hc.created_by AS created_by,
    hc.created_on AS created_on
	FROM
		hotelweb_cleaning AS hc
    INNER JOIN hotelweb_workers AS hw
			ON hc.worker_id=hw.worker_id
		INNER JOIN hotelweb_facilities AS hf
			ON hr.room_id=hc.facility_id;

	--Orders list view
	CREATE VIEW ordersView AS
	SELECT
	  ho.order_id AS order_id,
	  ho.order_time AS order_time,
	  ho.menu_id AS menu_id,
	  hm.item_name AS menu_name,
	  ho.order_time AS order_time,
	  ho.order_status AS order_status,
	  ho.paid AS paymenent_status,
	  ho.created_by AS guest_id,
	  hu.name AS guest_name,
	  hu.name AS ordered_by,
	  ho.created_on as created_on,
	FROM
	  hotelweb_orders AS ho
	INNER JOIN hotelweb_users AS hu
	  ON ho.created_by= hu.user_id
	INNER JOIN hotelweb_menu AS hm
	  ON ho.menu_id AS hm.menu_id


