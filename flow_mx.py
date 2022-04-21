########################################## INICIO Confirmar visita 48 hs antes MX ####################################################

from flow_modelo import CANCELATION_MOTIVE_SELECT, CLOSE_CLIENT, COMMERCIAL_AGENT_GROUP, CONFIRM_BOOKING_4_HOURS_BEFORE, CONFIRM_BOOKING_LESS_24_HOURS, COORDINATE_VISIT, COORDINATE_VISIT_BOOKER, NOTIFY_ALLIANCE_WHATSAPP, SEND_CONFIRMATION_WHATSAPP, SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED, create_action_state, create_task_state, get_close_case_callback, get_create_task_callback, get_create_task_callback_without_sla, get_metadata


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

###### Inicio Vertical No contestó #######

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

###### Fin vertical no contestó ######

###### Inicio vertical contestó ######
# State Contestó
state_replied = create_option_state(
    key="replied",
    name="Contestó",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Quiere confirmar la visita?"
    )
)

# State Confirmó visita
state_visit_confirmed = create_option_state(
    key="visit_confirmed",
    name="Confirmó visita",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State No podía hablar
state_could_not_talk = create_option_state(
    key="could_not_talk",
    name="No podía hablar",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

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

# State Cliente cancelo la visita
state_client_canceled = create_option_state(
    key="client_canceled",
    name="Cliente",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Alianza cancelo la visita
state_alliance_canceled = create_option_state(
    key="alliance_canceled",
    name="Alianza/Inmobiliaria",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata()
)

# State Asesor de mudafy cancelo la visita
state_mudafy_adviser_canceled = create_option_state(
    key="mudafy_adviser_canceled",
    name="Asesor Mudafy",
    flow=confirm_booking_24_hours_before,
    metadata=get_metadata()
)

# State Notificar a Alianza por whatsapp
state_notify_alliance_whatsapp = create_task_state(
    key=NOTIFY_ALLIANCE_WHATSAPP,
    name="Notificar a Alianza por whatsapp",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(
        title="¿Se envió un whatsapp?"
    )
)

# State Coordinar visita AC MX
state_coordinate_visit_AC_MX = create_task_state(
    key=COORDINATE_VISIT,
    name="Coordinar visita AC MX",
    flow=confirm_booking_48_hours_before,
    metadata=get_metadata(),
    is_state_final=True
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

# Edge inicial a No contestó
edge_0 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_replied,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge entre Contestó y Canceló visita
edge_13 = Edge.objects.create(
    from_state=state_replied,
    to_state=state_visit_canceled,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge entre Contestó y Confirmó visita
edge_6_1 = Edge.objects.create(
    from_state=state_replied,
    to_state=state_visit_confirmed,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=3,
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

# Edge entre Canceló visita y Cancelo el cliente
edge_18 = Edge.objects.create(
    from_state=state_cancel_visit,
    to_state=state_client_canceled,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=1,
)

# Edge entre Canceló visita y Cancelo la alianza
edge_18 = Edge.objects.create(
    from_state=state_cancel_visit,
    to_state=state_alliance_canceled,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=2,
)

# Edge entre Canceló visita y Cancelo el asesor de Mudafy
edge_18 = Edge.objects.create(
    from_state=state_cancel_visit,
    to_state=state_mudafy_adviser_canceled,
    flow=confirm_booking_48_hours_before,
    callbacks=[],
    order=3,
)

# Edge entre Cancelo el cliente y Colocal rol asignado
edge_18 = Edge.objects.create(
    from_state=state_alliance_canceled,
    to_state=state_notify_alliance_whatsapp,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        # Nahue
        get_create_task_callback(kind=NOTIFY_ALLIANCE_WHATSAPP, sla={"minutes": 30}, title="Notificar a Alianza por whatsapp")
    ],
    order=1,
)

# Edge entre Cancelo la alianza y Colocal rol asignado
edge_18 = Edge.objects.create(
    from_state=state_visit_canceled,
    to_state=state_notify_alliance_whatsapp,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        # Nahue
        get_create_task_callback(kind=NOTIFY_ALLIANCE_WHATSAPP, sla={"minutes": 30}, title="Notificar a Alianza por whatsapp")
    ],
    order=2,
)

# Edge entre Cancelo el asesor de Mudafy y Colocal rol asignado
edge_18 = Edge.objects.create(
    from_state=state_mudafy_adviser_canceled,
    to_state=state_notify_alliance_whatsapp,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        # Nahue
        get_create_task_callback(kind=NOTIFY_ALLIANCE_WHATSAPP, sla={"minutes": 30}, title="Notificar a Alianza por whatsapp")
    ],
    order=3,
)

# Edge entre Colocal rol asignado y Coordinar visita AC MX
edge_19 = Edge.objects.create(
    from_state=state_visit_canceled,
    to_state=state_coordinate_visit_AC_MX,
    flow=confirm_booking_48_hours_before,
    callbacks=[
        get_create_task_callback(kind=COORDINATE_VISIT, sla={"hours": 2}, title="Coordinar visita AC MX")
    ],
    order=1,
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

######### FIN Vertical Contesto ############

########################################## FIN Confirmar visita 48 hs antes MX ####################################################

####################### INICIO Enviar WA de confirmación MX AR ############################

send_whatsapp_confirmation = create_task_flow(name="Enviar WA de confirmación", subtype=SEND_WHATSAPP_BOOKING_CONFIRM_24, countries=["MX", "AR"])

initial_state = create_task_state(
    key=SEND_WHATSAPP_BOOKING_CONFIRM_24,
    name="Enviar WA de confirmación",
    flow=send_whatsapp_confirmation,
    metadata=get_metadata(
        title="¿Se envió whatsapp?"
    ),
)
send_whatsapp_confirmation.initial_state_id=initial_state.id
send_whatsapp_confirmation.save()

# State No se envió WA
state_whatsapp_not_sent = create_option_state(
    key="whatsapp_not_sent",
    name="No se envió",
    flow=send_whatsapp_confirmation,
    metadata=get_metadata()
)

# State Se envió WA
state_whatsapp_sent = create_option_state(
    key="whatsapp_sent",
    name="Se envió",
    flow=send_whatsapp_confirmation,
    metadata=get_metadata()
)

# State Confirmar visita 24 hrs antes
state_confirm_booking_less_24_hrs = create_task_state(
    key=CONFIRM_BOOKING_LESS_24_HOURS,
    name="Confirmar visita 24 hrs antes",
    flow=send_whatsapp_confirmation,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge entre Enviar WA de confirmación y Se envió WA
edge_1 = Edge.objects.create(
    from_state=state_send_whatsapp_for_confirmation,
    to_state=state_whatsapp_sent,
    flow=send_whatsapp_confirmation,
    callbacks=[],
    order=2,
)

# Edge entre Enviar WA de confirmación y No se envió WA
edge_2 = Edge.objects.create(
    from_state=state_send_whatsapp_for_confirmation,
    to_state=state_whatsapp_not_sent,
    flow=send_whatsapp_confirmation,
    callbacks=[],
    order=1,
)

# Edge de vuelta entre No se envió WA y Enviar WA de confirmación
edge_3 = Edge.objects.create(
    from_state=state_whatsapp_not_sent,
    to_state=state_send_whatsapp_for_confirmation,
    flow=send_whatsapp_confirmation,
    callbacks=[
        get_create_task_callback(kind=SEND_CONFIRMATION_WHATSAPP, sla={"minutes": 30}, title="Enviar whatsapp de confirmación")
    ],
    order=1,
)

# Edge entre Se envió WA y Confirmar visita 24 hrs antes
edge_4 = Edge.objects.create(
    from_state=state_whatsapp_sent,
    to_state=state_confirm_booking_less_24_hrs,
    flow=send_whatsapp_confirmation,
    callbacks=[
        get_create_task_callback_without_sla(kind=CONFIRM_BOOKING_LESS_24_HOURS, title="Confirmar visita 24 hrs antes")
    ],
    order=1,
)

################### FIN Enviar WA de confirmación ###########################

################### INICIO Enviar  WA de confirmación (despues de confirmar visita) #####################

send_whatsapp_confirmation_when_booked = create_task_flow(name="Enviar WA de confirmación", subtype=SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED, countries=["MX", "AR"])

initial_state = create_task_state(
    key=SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED,
    name="Enviar WA de confirmación",
    flow=send_whatsapp_confirmation_when_booked,
    metadata=get_metadata(
        title="¿Se envió whatsapp?"
    ),
)
send_whatsapp_confirmation_when_booked.initial_state_id=initial_state.id
send_whatsapp_confirmation_when_booked.save()

# State No se envió WA (despues de confirmar visita)
state_when_booked_whatsapp_not_sent = create_option_state(
    key="when_booked_whatsapp_not_sent",
    name="No se envió",
    flow=send_whatsapp_confirmation_when_booked,
    metadata=get_metadata()
)

# State Se envió WA (despues de confirmar visita)
state_when_booked_whatsapp_sent = create_option_state(
    key="when_booked_whatsapp_sent",
    name="Se envió",
    flow=send_whatsapp_confirmation_when_booked,
    metadata=get_metadata()
)

# State Enviar WA de confirmación (despues de confirmar visita)
state_confirm_booking_4_hrs = create_task_state(
    key=CONFIRM_BOOKING_4_HOURS_BEFORE,
    name="Confirmar visita 4 hrs antes",
    flow=send_whatsapp_confirmation_when_booked,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge entre Enviar WA de confirmación (despues de confirmar visita) y Se envió
edge_7 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_when_booked_whatsapp_sent,
    flow=send_whatsapp_confirmation_when_booked,
    callbacks=[],
    order=2,
)

# Edge entre Enviar WA de confirmación (despues de confirmar visita) y No se envió
edge_8 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_when_booked_whatsapp_not_sent,
    flow=send_whatsapp_confirmation_when_booked,
    callbacks=[],
    order=1,
)

# Edge de vuelta entre No se envió y Enviar WA de confirmación (despues de confirmar visita)
edge_9 = Edge.objects.create(
    from_state=state_when_booked_whatsapp_not_sent,
    to_state=state_when_booked_send_whatsapp_for_confirmation,
    flow=send_whatsapp_confirmation_when_booked,
    callbacks=[
        get_create_task_callback(kind=SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED, sla={"minutes": 30}, title="Enviar whatsapp de confirmación")
    ],
    order=1,
)

# Edge entre Se envió y Confirmar visita 4 hrs antes
edge_10 = Edge.objects.create(
    from_state=state_when_booked_whatsapp_sent,
    to_state=state_confirm_booking_4_hrs,
    flow=send_whatsapp_confirmation_when_booked,
    callbacks=[
        get_create_task_callback_without_sla(kind=CONFIRM_BOOKING_4_HOURS_BEFORE, title="Confirmar visita 4hrs antes")
    ],
    order=1,
)

################### FIN Enviar  WA de confirmación (despues de confirmar visita) #####################

################### INICIO Notificar a Alianza por WA MX ###############################

notify_alliances_with_whatsapp = create_task_flow(name="Notificar a Alianza por whatsapp", subtype=SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED, countries=["MX"])

initial_state = create_task_state(
    key=SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED,
    name="Notificar a Alianza por whatsapp",
    flow=notify_alliances_with_whatsapp,
    metadata=get_metadata(
        title="¿Se envió whatsapp?"
    ),
)
notify_alliances_with_whatsapp.initial_state_id=initial_state.id
notify_alliances_with_whatsapp.save()

# State No se envió
state_notification_not_sent = create_option_state(
    key="notification_not_sent",
    name="No se envió",
    flow=notify_alliances_with_whatsapp,
    metadata=get_metadata()
)

# State Se envió
state_notification_sent = create_option_state(
    key="state_notification_sent",
    name="Se envió",
    flow=notify_alliances_with_whatsapp,
    metadata=get_metadata()
)

#State Cerrar caso
state_close_case = create_task_state (
    key=CLOSE_CASE,
    name="Cerrar caso",
    flow=notify_alliances_with_whatsapp,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge entre Notificar a Alianza por WA y No se envió WA
edge_14 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_notification_not_sent,
    flow=notify_alliances_with_whatsapp,
    callbacks=[],
    order=1,
)

# Edge entre Notificar a Alianza por WA y Se envió WA
edge_15 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_notification_sent,
    flow=notify_alliances_with_whatsapp,
    callbacks=[],
    order=2,
)

# Edge de vuelta entre No se envió WA y Notificar a Alianza por WA
edge_16 = Edge.objects.create(
    from_state=state_notification_not_sent,
    to_state=state_notify_alliance_whatsapp,
    flow=notify_alliances_with_whatsapp,
    callbacks=[
        get_create_task_callback(kind=NOTIFY_ALLIANCE_WHATSAPP, sla={"minutes": 30}, title="Notificar a Alianza por whatsapp")
    ],
    order=1,
)

# Edge entre Se envió WA y Cerrar caso
edge_17 = Edge.objects.create(
    from_state=state_notification_sent,
    to_state=state_close_case,
    flow=notify_alliances_with_whatsapp,
    callbacks=[
        get_close_case_callback()
    ],
    order=1,
)

################### FIN Notificar a Alianza por WA MX ###############################









































































########################################## INICIO Confirmar visita 48 hs antes AR ####################################################

from flow_modelo import CANCELATION_MOTIVE_SELECT, COMMERCIAL_AGENT_GROUP, CONFIRM_BOOKING_4_HOURS_BEFORE, CONFIRM_BOOKING_LESS_24_HOURS, COORDINATE_VISIT, COORDINATE_VISIT_BOOKER, NOTIFY_ALLIANCE_WHATSAPP, SEND_CONFIRMATION_WHATSAPP, SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED, create_action_state, create_task_state, get_close_case_callback, get_create_task_callback, get_create_task_callback_without_sla, get_metadata


confirm_booking_48_hours_before_ar = create_task_flow(name="Confirmar visita 48 hs antes", subtype=CONFIRM_BOOKING_48_HOURS_BEFORE, countries=["AR"])

initial_state = create_task_state(
    key=CONFIRM_BOOKING_48_HOURS_BEFORE,
    name="Enviar recordatorio WA Alianza",
    flow=confirm_booking_48_hours_before_ar,
    metadata=get_metadata(
        title="¿Contestó la llamada?"
    ),
)
confirm_booking_48_hours_before_ar.initial_state_id=initial_state.id
confirm_booking_48_hours_before_ar.save()

###### Inicio Vertical No contestó #######

# State No contestó
state_no_reply = create_option_state(
    key="no_reply",
    name="No contestó",
    flow=confirm_booking_48_hours_before_ar,
    metadata=get_metadata()
)

# State Enviar WA de confirmación
state_send_whatsapp_for_confirmation = create_task_state(
    key=SEND_CONFIRMATION_WHATSAPP,
    name="Enviar whatsapp de confirmación",
    flow=confirm_booking_48_hours_before_ar,
    metadata=get_metadata(
        title="¿Se envió el Whatsapp?"
    )
)

# Edge inicial a No contestó
edge_0 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_no_reply,
    flow=confirm_booking_48_hours_before_ar,
    callbacks=[],
    order=2,
)

# Edge entre No contestó y Enviar WA de confirmación
edge_0 = Edge.objects.create(
    from_state=state_no_reply,
    to_state=state_send_whatsapp_for_confirmation,
    flow=confirm_booking_48_hours_before_ar,
    callbacks=[
        get_create_task_callback(kind=SEND_CONFIRMATION_WHATSAPP, sla={"minutes": 30}, title="Enviar WA de confirmación")
    ],
    order=2,
)

###### Fin vertical no contestó ######

###### Inicio vertical contestó ######
# State Contestó
state_replied = create_option_state(
    key="replied",
    name="Contestó",
    flow=confirm_booking_48_hours_before_ar,
    metadata=get_metadata(
        title="¿Quiere confirmar la visita?"
    )
)

# State Confirmó visita
state_visit_confirmed = create_option_state(
    key="visit_confirmed",
    name="Confirmó visita",
    flow=confirm_booking_48_hours_before_ar,
    metadata=get_metadata()
)

# State No podía hablar
state_could_not_talk = create_option_state(
    key="could_not_talk",
    name="No podía hablar",
    flow=confirm_booking_48_hours_before_ar,
    metadata=get_metadata()
)

# State Canceló visita
state_visit_canceled = create_option_state(
    key="visit_canceled",
    name="Canceló visita",
    flow=confirm_booking_48_hours_before_ar,
    metadata=get_metadata(
        title="¿Quiere reagendar?"
    )
)

# State Cancelar visita
state_cancel_visit = create_option_state(
    key="cancel_visit",
    name="Cancelar visita",
    flow=confirm_booking_48_hours_before_ar,
    metadata=get_metadata(
        title="¿Por qué se cancela la visita?"
    )
)

# State colocar rol asignado
state_place_role = create_action_state(
    key="place_role",
    name="Colocar rol asignado",
    flow=confirm_booking_48_hours_before_ar,
    metadata={
        "title": "Colocar rol del asignado",
        "state_type": AGENT_AUTOCOMPLETE,
        "agent_group" : "BackOfficeGroup"
    }
)

# State colocar motivo de cancelación
state_cancelation_motive = create_action_state(
    key="cancelation_motive",
    name="Motivo de cancelación",
    flow=confirm_booking_48_hours_before_ar,
    metadata=get_metadata(state_type=CANCELATION_MOTIVE_SELECT)
)

# State Notificar a Alianza por whatsapp
state_notify_alliance_whatsapp = create_task_state(
    key=NOTIFY_ALLIANCE_WHATSAPP,
    name="Notificar a Alianza por whatsapp",
    flow=confirm_booking_48_hours_before_ar,
    metadata=get_metadata(
        title="¿Se envió un whatsapp?"
    )
)

# State Coordinar visita BO AR
state_coordinate_visit_BO_AR = create_task_state(
    key=COORDINATE_VISIT,
    name="Coordinar visita BO AR",
    flow=confirm_booking_48_hours_before_ar,
    metadata=get_metadata(),
    is_state_final=True
)

# State Enviar WA de confirmación (despues de confirmar visita)
state_when_booked_send_whatsapp_for_confirmation = create_task_state(
    key=SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED,
    name="Enviar whatsapp de confirmación",
    flow=confirm_booking_48_hours_before_ar,
    metadata=get_metadata(
        title="¿Se envió whatsapp?"
    )
)

# Edge inicial a No contestó
edge_0 = Edge.objects.create(
    from_state=initial_state,
    to_state=state_replied,
    flow=confirm_booking_48_hours_before_ar,
    callbacks=[],
    order=2,
)

# Edge entre Contestó y Canceló visita
edge_13 = Edge.objects.create(
    from_state=state_replied,
    to_state=state_visit_canceled,
    flow=confirm_booking_48_hours_before_ar,
    callbacks=[],
    order=2,
)

# Edge entre Contestó y Confirmó visita
edge_6_1 = Edge.objects.create(
    from_state=state_replied,
    to_state=state_visit_confirmed,
    flow=confirm_booking_48_hours_before_ar,
    callbacks=[],
    order=3,
)

# Edge entre Contestó y No podía hablar
edge_11 = Edge.objects.create(
    from_state=state_replied,
    to_state=state_could_not_talk,
    flow=confirm_booking_48_hours_before_ar,
    callbacks=[],
    order=1,
)

# Edge entre No podía hablar y Enviar WA de confirmación (despues de confirmar visita)
edge_12 = Edge.objects.create(
    from_state=state_could_not_talk,
    to_state=state_send_whatsapp_for_confirmation,
    flow=confirm_booking_48_hours_before_ar,
    callbacks=[
        get_create_task_callback(kind=SEND_CONFIRMATION_WHATSAPP, sla={"minutes": 30}, title="Enviar whatsapp de confiramción")
    ],
    order=1,
)

# Edge entre Canceló visita y Colocal rol asignado
edge_18 = Edge.objects.create(
    from_state=state_visit_canceled,
    to_state=state_place_role,
    flow=confirm_booking_48_hours_before_ar,
    callbacks=[],
    order=2,
)

# Edge entre Colocal rol asignado y Coordinar visita AC MX
edge_19 = Edge.objects.create(
    from_state=state_place_role,
    to_state=state_coordinate_visit_BO_AR,
    flow=confirm_booking_48_hours_before_ar,
    callbacks=[
        get_create_task_callback(kind=COORDINATE_VISIT, sla={"hours": 2}, title="Coordinar visita BO AR")
    ],
    order=1,
)

# Edge entre Cancelar visita y Colocal motivo de cancelación
edge_20 = Edge.objects.create(
    from_state=state_cancel_visit,
    to_state=state_cancelation_motive,
    flow=confirm_booking_48_hours_before_ar,
    callbacks=[],
    order=1,
)

# Edge entre Cancelar visita y Colocal motivo de cancelación
edge_20 = Edge.objects.create(
    from_state=state_cancelation_motive,
    to_state=state_notify_alliance_whatsapp,
    flow=confirm_booking_48_hours_before_ar,
    callbacks=[
        # Callback de Nahue
        # get_create_task_callback_without_sla(kind=CANCEL_BOOKING, title="Cancelar visita"),
        get_create_task_callback(kind=NOTIFY_ALLIANCE_WHATSAPP, sla={"minutes": 30}, title="Notificar a Alianza por whatsapp")
    ],
    order=1,
)

# Edge entre Confirmó visita y Enviar WA de confirmación (despues de confirmar visita)
edge_6 = Edge.objects.create(
    from_state=state_visit_confirmed,
    to_state=state_when_booked_send_whatsapp_for_confirmation,
    flow=confirm_booking_48_hours_before_ar,
    callbacks=[
        get_create_task_callback(kind=SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED, sla={"minutes": 30}, title="Enviar whatsapp de confiramción")
    ],
    order=1,
)

######### FIN Vertical Contesto ############

########################################## FIN Confirmar visita 48 hs antes AR ####################################################


################### INICIO Notificar a Alianza por WA AR ###############################

notify_alliances_with_whatsapp_ar = create_task_flow(name="Notify Alliances sendig Whatsapp", subtype=SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED, countries=["MX"])

# State No se envió
state_notification_not_sent = create_option_state(
    key="notification_not_sent",
    name="No se envió",
    flow=notify_alliances_with_whatsapp_ar,
    metadata=get_metadata()
)

# State Se envió
state_notification_sent = create_option_state(
    key="state_notification_sent",
    name="Se envió",
    flow=notify_alliances_with_whatsapp_ar,
    metadata=get_metadata()
)

#State Cerrar caso
state_close_client = create_task_state (
    key=CLOSE_CLIENT,
    name="Cerrar caso",
    flow=notify_alliances_with_whatsapp_ar,
    metadata=get_metadata(),
    is_final_state=True
)

# Edge entre Notificar a Alianza por WA y No se envió WA
edge_14 = Edge.objects.create(
    from_state=state_notify_alliance_whatsapp,
    to_state=state_notification_not_sent,
    flow=notify_alliances_with_whatsapp_ar,
    callbacks=[],
    order=1,
)

# Edge entre Notificar a Alianza por WA y Se envió WA
edge_15 = Edge.objects.create(
    from_state=state_notify_alliance_whatsapp,
    to_state=state_notification_sent,
    flow=notify_alliances_with_whatsapp_ar,
    callbacks=[],
    order=2,
)

# Edge de vuelta entre No se envió WA y Notificar a Alianza por WA
edge_16 = Edge.objects.create(
    from_state=state_notification_not_sent,
    to_state=state_notify_alliance_whatsapp,
    flow=notify_alliances_with_whatsapp_ar,
    callbacks=[
        get_create_task_callback(kind=NOTIFY_ALLIANCE_WHATSAPP, sla={"minutes": 30}, title="Notificar a Alianza por whatsapp")
    ],
    order=1,
)

# Edge entre Se envió WA y Cerrar caso
edge_17 = Edge.objects.create(
    from_state=state_notification_sent,
    to_state=state_close_case,
    flow=notify_alliances_with_whatsapp_ar,
    callbacks=[
        get_close_client_callback()
    ],
    order=1,
)

################### FIN Notificar a Alianza por WA AR ###############################
