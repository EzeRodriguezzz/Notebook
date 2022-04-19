################################################ INICIO MÉTODOS AUXILIARES ###########################################################

FIRST_COMMERCIAL_CONTACT = "first_commercial_contact"

SEND_WHATSAPP = "send_whatsapp"
SEND_SECOND_WHATSAPP = "send_second_whatsapp"
SEND_THIRD_WHATSAPP = "send_third_whatsapp"
SEND_CONFIRMATION_WHATSAPP = "send_confirmation_whatsapp"
SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED = "send_confirmation_whatsapp_when_booked"
SEND_CLOSE_WHATSAPP = "send_close_whatsapp"
SEND_EMAIL = "send_email"
SEND_REMEMBER_ALLIANCE = "send_remember_alliance"
SEND_REMEMBER_ALLIANCE_BOOKER = "send_remember_alliance_booker"
SEND_FEEDBACK = "send_feedback"
SEND_COMMERCIAL_REPORT = "send_commercial_report"
SUGGEST_PROPERTIES = "suggest_properties"

FOLLOW_UP = "follow_up"
FOLLOW_UP_EMAIL = "follow_up_email"
FOLLOW_UP_WHATSAPP = "follow_up_whatsapp"
FOLLOW_UP_SECOND_WHATSAPP = "follow_up_second_whatsapp"
FOLLOW_UP_THIRD_WHATSAPP = "follow_up_third_whatsapp"
FOLLOW_UP_COORDINATE_VISIT = "follow_up_coordinate_visit"
FOLLOW_UP_SUGGEST_PROPERTIES = "follow_up_suggest_properties"
FOLLOW_UP_DEVELOPMENT = "follow_up_development"
FOLLOW_UP_BOOKING = "follow_up_booking"
FOLLOW_UP_BOOKING_PROPERTY = "follow_up_booking_property"
FOLLOW_UP_COUNTEROFFER = "follow_up_counteroffer"

NOTIFY_ALLIANCE_WHATSAPP = "notify_alliance_whatsapp"

FIRST_CALL = "first_call"
SECOND_CALL = "second_call"
THIRD_CALL = "third_call"

GENERATE_COMMERCIAL_REPORT = "generate_commercial_report"
SEARCH_PROPERTIES = "search_properties"
OFFER_PROPERTY = "offer_property"
CLOSE_OFFER = "close_offer"

COORDINATE_VISIT = "coordinate_visit"
COORDINATE_VISIT_BOOKER = "coordinate_visit_booker"
COORDINATE_WITH_ALLIANCE = "coordinate_with_alliance"
BOOK_VISIT = "book_visit"
RESEND_COORDINATE_VISIT_WHATSAPP = "resend_coordinate_visit_whatsapp"
DERIVATE_TO_BOOKER = "derivate_to_booker"
CREATE_BOOKING = "create_booking"
FEEDBACK_BOOKING = "feedback_booking"

CONFIRM_BOOKING_48_HOURS_BEFORE = "confirm_booking_48_hours_before"
CONFIRM_BOOKING_BETWEEN_48_AND_24_HOURS = "confirm_booking_between_48_and_24_hours"
CONFIRM_BOOKING_LESS_24_HOURS = "confirm_booking_less_24_hours"
CONFIRM_BOOKING_4_HOURS_BEFORE = "confirm_booking_4_hrs_before"

RETRY_FIRST_COMMERCIAL_CONTACT = "retry_first_commercial_contact"
PROFILE_CLIENT = "profile_client"

CLOSE_CLIENT = "close_client"
CLOSE_CASE = "close_case"
SENT = "sent"
NOT_SENT = "not_sent"
ANSWERED = "answered"
NOT_ANSWERED = "not_answered"
NOT_FOUND_ANSWER = "not_found_answered"
LOST_INTEREST = "lost_interest"
YES = "yes"

TASK = "task"
OPTION = "option"
ACTION = "action"

DATE_SELECT = "date-select"
CLOSING_CLIENT_SELECT = "closing-client-select"
CANCELATION_MOTIVE_SELECT = "cancelation-motive-select"
AGENT_AUTOCOMPLETE = "agent-autocomplete"
BOOKING_FORM = "booking-form"

ACTIVE="active"
CREATE_NEXT_TASK = "create_next_task"
SET_PROFILING = "set_profiling"
ADVANCE_IN_FUNNEL_CALLBACK = "advance_in_funnel"

UNREACHED = "unreached"
PITCHED = "pitched"
SCHEDULED = "scheduled"
PROPOSAL_MADE = "proposal_made"
LISTED = "listed"
CONSULTED = "consulted"
RESERVED = "reserved"
RESERVE_ACCEPTED = "reserve_accepted"
SOLD = "sold"
POST_SOLD = "post_sold"
CLOSED = "closed"

SEND_EMAIL_TEMPLATE = "send_email_template"
SEND_WHATSAPP_TEMPLATE = "send_whatsapp_template"
SEND_SECOND_WHATSAPP_TEMPLATE = "send_second_whatsapp_template"
SEND_THIRD_WHATSAPP_TEMPLATE = "send_third_whatsapp_template"
FOLLOW_UP_SUGGEST_PROPERTIES_TEMPLATE = "follow_up_suggest_properties_template"
SEND_CLOSE_WHATSAPP_TEMPLATE = "send_close_whatsapp_template"

AGENT_GROUP = "AgentGroup"
CONTROL_TOWER_GROUP = "ControlTowerGroup"
ON_SITE_ANALYST_GROUP = "OnSiteAnalystGroup"
COMMERCIAL_AGENT_GROUP = "CommercialAgentGroup"
CLIENT_GROUP = "ClientGroup"
OBSERVER_GROUP = "ObserverGroup"
MULTIMEDIA_GROUP = "MultimediaGroup"
MANAGER_GROUP = "ManagerGroup"
LEGAL_AGENT_GROUP = "LegalAgentGroup"
COMMERCIAL_CONTROL_TOWER_GROUP = "CommercialControlTowerGroup"
BACKOFFICE_GROUP = "BackOfficeGroup"
NO_GROUP = "NoGroup"

def get_create_task_callback(kind, sla, title):
    return {
        "name": CREATE_NEXT_TASK,
        "args": {
            "kind": kind,
            "sla": sla,
            "title": title
        }
    }

def get_create_task_callback_without_sla(kind, title):
    return {
        "name": CREATE_NEXT_TASK,
        "args": {
            "kind": kind,
            "title": title
        }
    }

def get_close_client_callback():
    return {
        "name": CLOSE_CLIENT,
        "args": {}
    }

def get_close_case_callback():
    return {
        "name": CLOSE_CASE,
        "args": {}
    }

def get_create_booking_callback():
    return {
        "name": CREATE_BOOKING,
        "args": {}
    }

def get_set_profiling_callback(profiling):
    return {
        "name": SET_PROFILING,
        "args": {
            "profiling": profiling
        }
    }

def get_advanced_stage_callback(stage):
    return {
        "name": ADVANCE_IN_FUNNEL_CALLBACK,
        "args": {
            "stage": stage
        }
    }

def get_metadata(state_type=OPTION, title="", next_action=None):
    if next_action:
        return {
            "title": title,
            "state_type": state_type,
            "next_action": next_action
        }
    else:
        return {
            "title": title,
            "state_type": state_type
        }

def create_task_flow(name, subtype, countries=["AR", "MX"], whatsapp_template_metadata={},roles=[COMMERCIAL_CONTROL_TOWER_GROUP,COMMERCIAL_AGENT_GROUP]):
    return Flow.objects.create(
        name=name,
        type=TASK,
        subtype=subtype,
        version=1,
        status=ACTIVE,
	        roles=roles,
        countries=countries,
        metadata=whatsapp_template_metadata
    )

def create_task_state(key, name, flow, metadata, is_final_state=False):
    return State.objects.create(
        key=key,
        name=name,
        kind=TASK,
        flow=flow,
        metadata=metadata,
        is_final_state=is_final_state
    )

def create_option_state(key, name, flow, metadata, is_final_state=False):
    return State.objects.create(
        key=key,
        name=name,
        kind=OPTION,
        flow=flow,
        metadata=metadata,
        is_final_state=is_final_state
    )

def create_action_state(key, name, flow, metadata, is_final_state=False):
    return State.objects.create(
        key=key,
        name=name,
        kind=ACTION,
        flow=flow,
        metadata=metadata,
        is_final_state=is_final_state
    )


################################################ FIN MÉTODOS AUXILIARES ###########################################################
############################################### INICIO NUEVA CONSULTA ###########################################################

first_commercial_contact_flow = create_task_flow(name="Nueva consulta", subtype=FIRST_COMMERCIAL_CONTACT)

initial_state = create_task_state(
    key=FIRST_COMMERCIAL_CONTACT,
    name="Nueva consulta",
    flow=first_commercial_contact_flow,
    metadata=get_metadata(
        title="¿Por qué canal estás contactándote?",
    ),
)
first_commercial_contact_flow.initial_state_id=initial_state.id
first_commercial_contact_flow.save()

#### Vertical de llamada ####
# State llamada
state_1 = create_option_state(
    key="call",
    name="Llamada",
    flow=first_commercial_contact_flow,
    metadata=get_metadata()
)

# State primer llamado
state_2 = create_task_state(
    key=FIRST_CALL,
    name="Primer llamado",
    flow=first_commercial_contact_flow,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge inicial
edge_0 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_1,
    flow=first_commercial_contact_flow,
    callbacks=[],
    order=1,
)

# Edge de entre llamada y primer llamado
edge_1 = Edge.objects.create(
    from_state=state_1,
    to_state=state_2,
    flow=first_commercial_contact_flow,
    callbacks=[get_create_task_callback(kind=FIRST_CALL, sla={"minutes":15}, title="Primer Llamado")],
    order=1,
)

#### Vertical de Whatsapp ####
# State Whatsappp
state_1 = create_option_state(
    key="whatsapp",
    name="Whatsapp",
    flow=first_commercial_contact_flow,
    metadata=get_metadata()
)

# State Envio WA
state_2 = create_task_state(
    key=SEND_WHATSAPP,
    name="Enviar Whatsapp",
    flow=first_commercial_contact_flow,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge inicial
edge_0 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_1,
    flow=first_commercial_contact_flow,
    callbacks=[],
    order=2,
)

# Edge de entre Whatsapp y Envio WA
edge_1 = Edge.objects.create(
    from_state=state_1,
    to_state=state_2,
    flow=first_commercial_contact_flow,
    callbacks=[get_create_task_callback(kind=SEND_WHATSAPP, sla={"minutes":15}, title="Enviar Whatsapp")],
    order=1,
)

#### Vertical de EMAIL ####
# State EMAIL
state_1 = create_option_state(
    key="email",
    name="Email",
    flow=first_commercial_contact_flow,
    metadata=get_metadata()
)

# State Envio Email
state_2 = create_task_state(
    key=SEND_EMAIL,
    name="Envío Email",
    flow=first_commercial_contact_flow,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge inicial
edge_0 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_1,
    flow=first_commercial_contact_flow,
    callbacks=[],
    order=3,
)

# Edge de entre EMAIL y Envio EMAIL
edge_1 = Edge.objects.create(
    from_state=state_1,
    to_state=state_2,
    flow=first_commercial_contact_flow,
    callbacks=[get_create_task_callback(kind=SEND_EMAIL, sla={"minutes":30}, title="Enviar Email")],
    order=1,
)

#### Vertical de Datos incorrectos ####
# State Datos incorrectos
state_1 = create_option_state(
    key="wrong_data",
    name="Datos incorrectos",
    flow=first_commercial_contact_flow,
    metadata=get_metadata(title="Colocar motivo de cierre del cliente", )
)

# State Seleccionar motivo de cierre
state_2 = create_action_state(
    key="select_closing_client_reason",
    name="Seleccionar motivo de cierre",
    flow=first_commercial_contact_flow,
    metadata=get_metadata(state_type=CLOSING_CLIENT_SELECT),
)

# State Cerrar cliente
state_3 = create_option_state(
    key=CLOSE_CLIENT,
    name="Cerrar cliente",
    flow=first_commercial_contact_flow,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge inicial
edge_0 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_1,
    flow=first_commercial_contact_flow,
    callbacks=[],
    order=4,
)

# Edge de entre Datos incorrectos y Seleccionar motivo de cierre
edge_1 = Edge.objects.create(
    from_state=state_1,
    to_state=state_2,
    flow=first_commercial_contact_flow,
    callbacks=[],
    order=1,
)

# Edge de entre Seleccionar motivo de cierre y Cerrar cliente
edge_1 = Edge.objects.create(
    from_state=state_2,
    to_state=state_3,
    flow=first_commercial_contact_flow,
    callbacks=[get_close_client_callback()],
    order=1,
)

############################################### FIN NUEVA CONSULTA ###########################################################

############################################### INICIO AGENDAR VISITA ###########################################################

booking_visit = create_task_flow(name="Agendar visita", subtype=BOOK_VISIT,countries=["AR", "MX"], whatsapp_template_metadata={},roles=[COMMERCIAL_AGENT_GROUP])

initial_state = create_task_state(
    key=BOOK_VISIT,
    name="Agendar visita",
    flow=booking_visit,
    metadata=get_metadata(
        title="¿El cliente reconfirma asistencia?"
    ),
)
booking_visit.initial_state_id=initial_state.id
booking_visit.save()

#### Inicio Vertical No puede ####
# State No puede
state_no = create_option_state(
    key="no",
    name="No puede",
    flow=booking_visit,
    metadata=get_metadata()
)

#State seleccionar fecha
state_select_date_custom = create_action_state(
    key="select_date",
    name="Seleccionar fecha",
    flow=booking_visit,
    metadata=get_metadata(state_type=DATE_SELECT)
)

# State No puede
state_coordinate_visit = create_task_state(
    key=COORDINATE_VISIT,
    name="Coordinar visita",
    flow=booking_visit,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge de entre Agendar visita y No puede
edge_1 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_no,
    flow=booking_visit,
    callbacks=[],
    order=2
)

# Edge de entre No puede y Seleccionar Fecha
edge_22 = Edge.objects.create(
    from_state=state_no,
    to_state=state_select_date_custom,
    flow=booking_visit,
    callbacks=[],
    order=2
)

# Edge de entre Seleccionar Fecha y Enviar WhatsApp para volver a coordinar
edge_33 = Edge.objects.create(
	    from_state=state_select_date_custom,
    to_state=state_coordinate_visit,
    flow=booking_visit,
    callbacks=[
        get_create_task_callback_without_sla(kind=COORDINATE_VISIT,  title="Coordinar visita")
    ],
    order=1,
)

#### Inicio Vertical Sí, asistirá ####
# State Sí, asistirá
state_yes = create_option_state(
    key="yes",
    name="Confirmó",
    flow=booking_visit,
    metadata=get_metadata(title="Ingrese la información del booking")
)

# State Booking
state_booking = create_action_state(
    key="booking-form",
    name="Creación de booking",
    flow=booking_visit,
    metadata=get_metadata(title="¿El cliente tiene pendiente otra propiedad para coordinar visita?", state_type=BOOKING_FORM)
)

# Edge de entre Agendar visita y Sí, asistirá
edge_3 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_yes,
    flow=booking_visit,
    callbacks=[],
    order=1
)

# Edge de entre Sí, asistirá y Booking
edge_4 = Edge.objects.create(
    from_state=state_yes,
    to_state=state_booking,
    flow=booking_visit,
    callbacks=[],
    order=1
)

#### Inicio Vertical Si (coordinar visita) ####
# State Si (coordinar visita)
state_yes_to_coordinate_visit = create_option_state(
    key="yes",
    name="Sí",
    flow=booking_visit,
    metadata=get_metadata(title="¿El cliente quiere  buscar otras propiedades?")
)

# Edge de entre Booking y Si
edge_5 = Edge.objects.create(
    from_state=state_booking,
    to_state=state_yes_to_coordinate_visit,
    flow=booking_visit,
    callbacks=[
        get_create_booking_callback()
    ],
    order=1
)

# State Si (buscar nuevas propiedades)
state_yes_to_search_properties = create_option_state(
    key="yes",
    name="Sí",
    flow=booking_visit,
    metadata=get_metadata(title="¿Para cuando queres el recordatorio?")
)

# State No (buscar nuevas propiedades)
state_no_to_search_properties = create_option_state(
    key="no",
    name="No",
    flow=booking_visit,
    metadata=get_metadata(title="¿Para cuando queres el recordatorio?")
)

# State Seleccionar fecha
state_select_date = create_action_state(
    key="select_date",
    name="Seleccionar fecha",
    flow=booking_visit,
    metadata=get_metadata(state_type=DATE_SELECT),
)

# State Enviar recordatorio WA Alianza
state_remember_alliance = create_task_state(
    key=SEND_REMEMBER_ALLIANCE,
    name="Enviar recordatorio Alianza",
    flow=booking_visit,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge de entre Sí (coordinar visita) y No (buscar propiedades)
edge_6 = Edge.objects.create(
    from_state=state_yes_to_coordinate_visit,
    to_state=state_no_to_search_properties,
    flow=booking_visit,
    callbacks=[
        get_create_task_callback(kind=COORDINATE_VISIT, sla={"hours":12}, title="Coordinar visita")
    ],
    order=1
)

# Edge de entre Sí (coordinar visita) y Sí (buscar propiedades)
edge_7 = Edge.objects.create(
    from_state=state_yes_to_coordinate_visit,
    to_state=state_yes_to_search_properties,
    flow=booking_visit,
    callbacks=[
        get_create_task_callback(kind=COORDINATE_VISIT, sla={"hours":12}, title="Coordinar visita")
    ],
    order=1
)

# Edge de entre Sí (buscar propiedades) y Seleccionar Fecha
edge_8 = Edge.objects.create(
    from_state=state_yes_to_search_properties,
    to_state=state_select_date,
    flow=booking_visit,
    callbacks=[
        get_create_task_callback(kind=SEARCH_PROPERTIES, sla={"hours":3}, title="Buscar propiedades")
    ],
    order=1
)

# Edge de entre  No (buscar propiedades) y Seleccionar Fecha
edge_9 = Edge.objects.create(
    from_state=state_no_to_search_properties,
    to_state=state_select_date,
    flow=booking_visit,
    callbacks=[],
    order=1
)

# Edge de entre Seleccionar Fecha y Enviar recordatorio WA Alianza
edge_10 = Edge.objects.create(
    from_state=state_select_date,
    to_state=state_remember_alliance,
    flow=booking_visit,
    callbacks=[
        get_create_task_callback(kind=SEND_REMEMBER_ALLIANCE, sla={"minutes":30}, title="Enviar recordatorio Alianza")
    ],
    order=1
)

# State No (coordinar visita)
state_no_to_coordinate_visit = create_option_state(
    key="no",
    name="No",
    flow=booking_visit,
    metadata=get_metadata(title="¿El cliente quiere  buscar otras propiedades?")
)

# Edge de entre Booking y No
edge_10 = Edge.objects.create(
    from_state=state_booking,
    to_state=state_no_to_coordinate_visit,
    flow=booking_visit,
    callbacks=[
        get_create_booking_callback()
    ],
    order=2
)

# Edge de entre No (coordinar visita) y No (buscar propiedades)
edge_12 = Edge.objects.create(
    from_state=state_no_to_coordinate_visit,
    to_state=state_no_to_search_properties,
    flow=booking_visit,
    callbacks=[],
    order=1
)

# Edge de entre No (coordinar visita) y Sí (buscar propiedades)
edge_13 = Edge.objects.create(
    from_state=state_no_to_coordinate_visit,
    to_state=state_yes_to_search_properties,
    flow=booking_visit,
    callbacks=[],
    order=1
)

################################################## FIN AGENDAR VISITA ###########################################################
########################################## INICIO Confirmar visita 48 hs antes AR ####################################################


confirm_booking_48_hours_before = create_task_flow(name="Confirmar visita 48 hs antes", subtype=CONFIRM_BOOKING_48_HOURS_BEFORE, countries=["MX"])

initial_state = create_task_state(
    key=CONFIRM_BOOKING_48_HOURS_BEFORE,
    name="Enviar recordatorio WA Alianza",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Contestó la llamada?"
    ),
)
confirm_booking_48_hours_before.initial_state_id=initial_state.id
confirm_booking_48_hours_before.save()

#### Inicio Vertical No contestó
# State No contestó
state_no_reply = create_option_state(
    key="no_reply",
    name="No contestó",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Enviar WA de confirmación
state_send_whatsapp_for_confirmation = create_task_state(
    key=SEND_CONFIRMATION_WHATSAPP,
    name="Enviar whatsapp de confirmación",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Se envió el Whatsapp?"
    )
)

# State No se envió WA
state_whatsapp_not_sent = create_option_state(
    key="whatsapp_not_sent",
    name="No se envió",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Se envió WA
state_whatsapp_sent = create_option_state(
    key="whatsapp_sent",
    name="Se envió",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Confirmar visita 24 hrs antes
state_confirm_booking_less_24_hrs = create_task_state(
    key=CONFIRM_BOOKING_LESS_24_HOURS,
    name="Confirmar visita 24 hrs antes",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge inicial a No contestó
edge_0 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_no_reply,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge entre No contestó y Enviar WA de confirmación
edge_0 = Edge.objects.create(
    from_state=state_no_reply,
    to_state=state_send_whatsapp_for_confirmation,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=SEND_CONFIRMATION_WHATSAPP, sla={"minutes": 30}, title="Enviar WA de confirmación")
    ],
    order=2,
)

# Edge entre Enviar WA de confirmación y Se envió WA
edge_1 = Edge.objects.create(
    from_state=state_send_whatsapp_for_confirmation,
    to_state=state_whatsapp_sent,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge entre Enviar WA de confirmación y No se envió WA
edge_2 = Edge.objects.create(
    from_state=state_send_whatsapp_for_confirmation,
    to_state=state_whatsapp_not_sent,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=1,
)

# Edge de vuelta entre No se envió WA y Enviar WA de confirmación
edge_3 = Edge.objects.create(
    from_state=state_whatsapp_not_sent,
    to_state=state_send_whatsapp_for_confirmation,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=SEND_CONFIRMATION_WHATSAPP, sla={"minutes": 30}, title="Enviar whatsapp de confirmación")
    ],
    order=1,
)

# Edge entre Se envió WA y Confirmar visita 24 hrs antes
edge_4 = Edge.objects.create(
    from_state=state_whatsapp_sent,
    to_state=state_confirm_booking_less_24_hrs,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback_without_sla(kind=CONFIRM_BOOKING_LESS_24_HOURS, title="Confirmar visita 24 hrs antes")
    ],
    order=1,
)

#### Vertical Contestó 
# State Contestó
state_replied = create_option_state(
    key="replied",
    name="Contestó",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Quiere confirmar la visita?"
    )
)


### Inicio Vertical Contestó > Canceló visita
# State Canceló visita
state_visit_canceled = create_option_state(
    key="visit_canceled",
    name="Canceló visita",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Quiere reagendar?"
    )
)

# State Cancelar visita
state_cancel_visit = create_option_state(
    key="cancel_visit",
    name="Cancelar visita",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Por qué se cancela la visita?"
    )
)

# State Cancelar visita
state_coordinate_visit_BO_AR = create_task_state(
    key=COORDINATE_VISIT,
    name="Coordinar visita BO AR",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(),
    is_final_state=True
)

# State Cancelar visita
state_notify_alliance_whatsapp = create_task_state(
    key=NOTIFY_ALLIANCE_WHATSAPP,
    name="Notificar a Alianza por whatsapp",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Se envió un whatsapp?"
    )
)

# State No se envió
state_notification_not_sent = create_option_state(
    key="notification_not_sent",
    name="No se envió",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Se envió
state_notification_sent = create_option_state(
    key="state_notification_sent",
    name="Se envió",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State colocar rol asignado
state_place_role = create_action_state(
    key="place_role",
    name="Colocar rol asignado",
    flow=confirm_booking_48_hours_before,
    metadata={
        "title": "Colocar rol del asesor",
        "state_type": AGENT_AUTOCOMPLETE,
        "agent_group" : "BackOfficeGroup"
    }
)

# State colocar motivo de cancelación
state_cancelation_motive = create_action_state(
    key="cancelation_motive",
    name="Motivo de cancelación",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(state_type=CANCELATION_MOTIVE_SELECT)
)

#State Cerrar caso
state_close_case = create_task_state (
    key=CLOSE_CASE,
    name="Cerrar caso",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge entre Contestó y Canceló visita
edge_13 = Edge.objects.create(
    from_state=state_replied,
    to_state=state_visit_canceled,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge entre Notificar a Alianza por WA y No se envió WA
edge_14 = Edge.objects.create(
    from_state=state_notify_alliance_whatsapp,
    to_state=state_notification_not_sent,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=1,
)

# Edge entre Notificar a Alianza por WA y Se envió WA
edge_15 = Edge.objects.create(
    from_state=state_notify_alliance_whatsapp,
    to_state=state_notification_sent,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge de vuelta entre No se envió WA y Notificar a Alianza por WA
edge_16 = Edge.objects.create(
    from_state=state_notification_not_sent,
    to_state=state_notify_alliance_whatsapp,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=NOTIFY_ALLIANCE_WHATSAPP, sla={"minutes": 30}, title="Notificar a Alianza por whatsapp")
    ],
    order=1,
)

# Edge entre Se envió WA y Cerrar caso
edge_17 = Edge.objects.create(
    from_state=state_notification_sent,
    to_state=state_close_case,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_close_case_callback()
    ],
    order=1,
)

# Edge entre Canceló visita y Colocal rol asignado
edge_18 = Edge.objects.create(
    from_state=state_visit_canceled,
    to_state=state_place_role,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge entre Colocal rol asignado y Coordinar visita BO AR
edge_19 = Edge.objects.create(
    from_state=state_place_role,
    to_state=state_coordinate_visit_BO_AR,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=COORDINATE_VISIT, sla={"hours": 2}, title="Coordinar visita BO AR")
    ],
    order=1,
)

# Edge entre Cancelar visita y Colocal motivo de cancelación
edge_20 = Edge.objects.create(
    from_state=state_cancel_visit,
    to_state=state_cancelation_motive,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=1,
)

# Edge entre Cancelar visita y Colocal motivo de cancelación
edge_20 = Edge.objects.create(
    from_state=state_cancelation_motive,
    to_state=state_notify_alliance_whatsapp,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=NOTIFY_ALLIANCE_WHATSAPP, sla={"minutes": 30}, title="Notificar a Alianza por whatsapp")
    ],
    order=1,
)


#### Inicio Vertical Contestó > Confirmó visita
# State Confirmó visita
state_visit_confirmed = create_option_state(
    key="visit_confirmed",
    name="Confirmó visita",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Enviar WA de confirmación (despues de confirmar visita)
state_when_booked_send_whatsapp_for_confirmation = create_task_state(
    key=SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED,
    name="Enviar whatsapp de confirmación",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Se envió whatsapp?"
    )
)

# State No se envió WA (despues de confirmar visita)
state_when_booked_whatsapp_not_sent = create_option_state(
    key="when_booked_whatsapp_not_sent",
    name="No se envió",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Se envió WA (despues de confirmar visita)
state_when_booked_whatsapp_sent = create_option_state(
    key="when_booked_whatsapp_sent",
    name="Se envió",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Enviar WA de confirmación (despues de confirmar visita)
state_confirm_booking_4_hrs = create_task_state(
    key=CONFIRM_BOOKING_4_HOURS_BEFORE,
    name="Confirmar visita 4 hrs antes",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge entre Contestó y Confirmó visita
edge_6_1 = Edge.objects.create(
    from_state=state_replied,
    to_state=state_visit_confirmed,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=3,
)

# Edge entre Confirmó visita y Enviar WA de confirmación (despues de confirmar visita)
edge_6 = Edge.objects.create(
    from_state=state_visit_confirmed,
    to_state=state_when_booked_send_whatsapp_for_confirmation,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED, sla={"minutes": 30}, title="Enviar whatsapp de confiramción")
    ],
    order=1,
)

# Edge entre Enviar WA de confirmación (despues de confirmar visita) y Se envió
edge_7 = Edge.objects.create(
    from_state=state_when_booked_send_whatsapp_for_confirmation,
    to_state=state_when_booked_whatsapp_sent,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge entre Enviar WA de confirmación (despues de confirmar visita) y No se envió
edge_8 = Edge.objects.create(
    from_state=state_when_booked_send_whatsapp_for_confirmation,
    to_state=state_when_booked_whatsapp_not_sent,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=1,
)

# Edge de vuelta entre No se envió y Enviar WA de confirmación (despues de confirmar visita)
edge_9 = Edge.objects.create(
    from_state=state_when_booked_whatsapp_not_sent,
    to_state=state_when_booked_send_whatsapp_for_confirmation,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED, sla={"minutes": 30}, title="Enviar whatsapp de confirmación")
    ],
    order=1,
)

# Edge entre Enviar WA de confirmación (despues de confirmar visita) y Confirmar visita 4 hrs antes
edge_10 = Edge.objects.create(
    from_state=state_when_booked_whatsapp_sent,
    to_state=state_confirm_booking_4_hrs,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback_without_sla(kind=CONFIRM_BOOKING_4_HOURS_BEFORE, title="Confirmar visita 4hrs antes")
    ],
    order=1,
)

#### Inicio vertical Contestó > No podía hablar
# State No podía hablar
state_could_not_talk = create_option_state(
    key="could_not_talk",
    name="No podía hablar",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# Edge entre Contestó y No podía hablar
edge_11 = Edge.objects.create(
    from_state=state_replied,
    to_state=state_could_not_talk,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=1,
)

# Edge entre Confirmó visita y Enviar WA de confirmación (despues de confirmar visita)
edge_12 = Edge.objects.create(
    from_state=state_could_not_talk,
    to_state=state_send_whatsapp_for_confirmation,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=SEND_CONFIRMATION_WHATSAPP, sla={"minutes": 30}, title="Enviar whatsapp de confiramción")
    ],
    order=1,
)

########################################## FIN Confirmar visita 48 hs antes MX ####################################################

########################################## INICIO Confirmar visita 48 hs antes MX ####################################################


confirm_booking_48_hours_before = create_task_flow(name="Confirmar visita 48 hs antes", subtype=CONFIRM_BOOKING_48_HOURS_BEFORE, countries=["MX"])

initial_state = create_task_state(
    key=CONFIRM_BOOKING_48_HOURS_BEFORE,
    name="Enviar recordatorio WA Alianza",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Contestó la llamada?"
    ),
)
confirm_booking_48_hours_before.initial_state_id=initial_state.id
confirm_booking_48_hours_before.save()

#### Inicio Vertical No contestó
# State No contestó
state_no_reply = create_option_state(
    key="no_reply",
    name="No contestó",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Enviar WA de confirmación
state_send_whatsapp_for_confirmation = create_task_state(
    key=SEND_CONFIRMATION_WHATSAPP,
    name="Enviar whatsapp de confirmación",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Se envió el Whatsapp?"
    )
)

# State No se envió WA
state_whatsapp_not_sent = create_option_state(
    key="whatsapp_not_sent",
    name="No se envió",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Se envió WA
state_whatsapp_sent = create_option_state(
    key="whatsapp_sent",
    name="Se envió",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Confirmar visita 24 hrs antes
state_confirm_booking_less_24_hrs = create_task_state(
    key=CONFIRM_BOOKING_LESS_24_HOURS,
    name="Confirmar visita 24 hrs antes",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge inicial a No contestó
edge_0 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_no_reply,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge entre No contestó y Enviar WA de confirmación
edge_0 = Edge.objects.create(
    from_state=state_no_reply,
    to_state=state_send_whatsapp_for_confirmation,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=SEND_CONFIRMATION_WHATSAPP, sla={"minutes": 30}, title="Enviar WA de confirmación")
    ],
    order=2,
)

# Edge entre Enviar WA de confirmación y Se envió WA
edge_1 = Edge.objects.create(
    from_state=state_send_whatsapp_for_confirmation,
    to_state=state_whatsapp_sent,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge entre Enviar WA de confirmación y No se envió WA
edge_2 = Edge.objects.create(
    from_state=state_send_whatsapp_for_confirmation,
    to_state=state_whatsapp_not_sent,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=1,
)

# Edge de vuelta entre No se envió WA y Enviar WA de confirmación
edge_3 = Edge.objects.create(
    from_state=state_whatsapp_not_sent,
    to_state=state_send_whatsapp_for_confirmation,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=SEND_CONFIRMATION_WHATSAPP, sla={"minutes": 30}, title="Enviar whatsapp de confirmación")
    ],
    order=1,
)

# Edge entre Se envió WA y Confirmar visita 24 hrs antes
edge_4 = Edge.objects.create(
    from_state=state_whatsapp_sent,
    to_state=state_confirm_booking_less_24_hrs,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback_without_sla(kind=CONFIRM_BOOKING_LESS_24_HOURS, title="Confirmar visita 24 hrs antes")
    ],
    order=1,
)

#### Vertical Contestó 
# State Contestó
state_replied = create_option_state(
    key="replied",
    name="Contestó",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Quiere confirmar la visita?"
    )
)


### Inicio Vertical Contestó > Canceló visita
# State Canceló visita
state_visit_canceled = create_option_state(
    key="visit_canceled",
    name="Canceló visita",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Quiere reagendar?"
    )
)

# State Cancelar visita
state_cancel_visit = create_option_state(
    key="cancel_visit",
    name="Cancelar visita",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Por qué se cancela la visita?"
    )
)

# State Cancelar visita
state_coordinate_visit_AC_MX = create_task_state(
    key=COORDINATE_VISIT,
    name="Coordinar visita AC MX",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(),
    is_state_final=True
)

# State Cancelar visita
state_notify_alliance_whatsapp = create_task_state(
    key=NOTIFY_ALLIANCE_WHATSAPP,
    name="Notificar a Alianza por whatsapp",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Se envió un whatsapp?"
    )
)

# State No se envió
state_notification_not_sent = create_option_state(
    key="notification_not_sent",
    name="No se envió",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Se envió
state_notification_sent = create_option_state(
    key="state_notification_sent",
    name="Se envió",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State colocar rol asignado
state_place_role = create_action_state(
    key="place_role",
    name="Colocar rol asignado",
    flow=confirm_booking_48_hours_before,
    metadata={
        "title": "Colocar rol del asesor",
        "state_type": AGENT_AUTOCOMPLETE,
        "agent_group" : "BackOfficeGroup"
    }
)

# State colocar motivo de cancelación
state_cancelation_motive = create_action_state(
    key="cancelation_motive",
    name="Motivo de cancelación",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(state_type=CANCELATION_MOTIVE_SELECT)
)

#State Cerrar caso
state_close_case = create_task_state (
    key=CLOSE_CASE,
    name="Cerrar caso",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge entre Contestó y Canceló visita
edge_13 = Edge.objects.create(
    from_state=state_replied,
    to_state=state_visit_canceled,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge entre Notificar a Alianza por WA y No se envió WA
edge_14 = Edge.objects.create(
    from_state=state_notify_alliance_whatsapp,
    to_state=state_notification_not_sent,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=1,
)

# Edge entre Notificar a Alianza por WA y Se envió WA
edge_15 = Edge.objects.create(
    from_state=state_notify_alliance_whatsapp,
    to_state=state_notification_sent,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge de vuelta entre No se envió WA y Notificar a Alianza por WA
edge_16 = Edge.objects.create(
    from_state=state_notification_not_sent,
    to_state=state_notify_alliance_whatsapp,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=NOTIFY_ALLIANCE_WHATSAPP, sla={"minutes": 30}, title="Notificar a Alianza por whatsapp")
    ],
    order=1,
)

# Edge entre Se envió WA y Cerrar caso
edge_17 = Edge.objects.create(
    from_state=state_notification_sent,
    to_state=state_close_case,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_close_case_callback()
    ],
    order=1,
)

# Edge entre Canceló visita y Colocal rol asignado
edge_18 = Edge.objects.create(
    from_state=state_visit_canceled,
    to_state=state_place_role,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge entre Colocal rol asignado y Coordinar visita AC MX
edge_19 = Edge.objects.create(
    from_state=state_place_role,
    to_state=state_coordinate_visit_AC_MX,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=COORDINATE_VISIT, sla={"hours": 2}, title="Coordinar visita AC MX")
    ],
    order=1,
)

# Edge entre Cancelar visita y Colocal motivo de cancelación
edge_20 = Edge.objects.create(
    from_state=state_cancel_visit,
    to_state=state_cancelation_motive,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=1,
)

# Edge entre Cancelar visita y Colocal motivo de cancelación
edge_20 = Edge.objects.create(
    from_state=state_cancelation_motive,
    to_state=state_notify_alliance_whatsapp,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=NOTIFY_ALLIANCE_WHATSAPP, sla={"minutes": 30}, title="Notificar a Alianza por whatsapp")
    ],
    order=1,
)



#### Inicio Vertical Contestó > Confirmó visita
# State Confirmó visita
state_visit_confirmed = create_option_state(
    key="visit_confirmed",
    name="Confirmó visita",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Enviar WA de confirmación (despues de confirmar visita)
state_when_booked_send_whatsapp_for_confirmation = create_task_state(
    key=SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED,
    name="Enviar whatsapp de confirmación",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Se envió whatsapp?"
    )
)

# State No se envió WA (despues de confirmar visita)
state_when_booked_whatsapp_not_sent = create_option_state(
    key="when_booked_whatsapp_not_sent",
    name="No se envió",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Se envió WA (despues de confirmar visita)
state_when_booked_whatsapp_sent = create_option_state(
    key="when_booked_whatsapp_sent",
    name="Se envió",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Enviar WA de confirmación (despues de confirmar visita)
state_confirm_booking_4_hrs = create_task_state(
    key=CONFIRM_BOOKING_4_HOURS_BEFORE,
    name="Confirmar visita 4 hrs antes",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge entre Contestó y Confirmó visita
edge_6_1 = Edge.objects.create(
    from_state=state_replied,
    to_state=state_visit_confirmed,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=3,
)

# Edge entre Confirmó visita y Enviar WA de confirmación (despues de confirmar visita)
edge_6 = Edge.objects.create(
    from_state=state_visit_confirmed,
    to_state=state_when_booked_send_whatsapp_for_confirmation,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED, sla={"minutes": 30}, title="Enviar whatsapp de confiramción")
    ],
    order=1,
)

# Edge entre Enviar WA de confirmación (despues de confirmar visita) y Se envió
edge_7 = Edge.objects.create(
    from_state=state_when_booked_send_whatsapp_for_confirmation,
    to_state=state_when_booked_whatsapp_sent,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge entre Enviar WA de confirmación (despues de confirmar visita) y No se envió
edge_8 = Edge.objects.create(
    from_state=state_when_booked_send_whatsapp_for_confirmation,
    to_state=state_when_booked_whatsapp_not_sent,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=1,
)

# Edge de vuelta entre No se envió y Enviar WA de confirmación (despues de confirmar visita)
edge_9 = Edge.objects.create(
    from_state=state_when_booked_whatsapp_not_sent,
    to_state=state_when_booked_send_whatsapp_for_confirmation,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED, sla={"minutes": 30}, title="Enviar whatsapp de confirmación")
    ],
    order=1,
)

# Edge entre Enviar WA de confirmación (despues de confirmar visita) y Confirmar visita 4 hrs antes
edge_10 = Edge.objects.create(
    from_state=state_when_booked_whatsapp_sent,
    to_state=state_confirm_booking_4_hrs,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback_without_sla(kind=CONFIRM_BOOKING_4_HOURS_BEFORE, title="Confirmar visita 4hrs antes")
    ],
    order=1,
)

#### Inicio vertical Contestó > No podía hablar
# State No podía hablar
state_could_not_talk = create_option_state(
    key="could_not_talk",
    name="No podía hablar",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# Edge entre Contestó y No podía hablar
edge_11 = Edge.objects.create(
    from_state=state_replied,
    to_state=state_could_not_talk,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=1,
)

# Edge entre No podía hablar y Enviar WA de confirmación (despues de confirmar visita)
edge_12 = Edge.objects.create(
    from_state=state_could_not_talk,
    to_state=state_send_whatsapp_for_confirmation,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=SEND_CONFIRMATION_WHATSAPP, sla={"minutes": 30}, title="Enviar whatsapp de confiramción")
    ],
    order=1,
)

########################################## FIN Confirmar visita 48 hs antes MX ####################################################