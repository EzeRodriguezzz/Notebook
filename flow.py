########################################## INICIO Confirmar visita 48 hs antes MX ####################################################

from flow_modelo import CONFIRM_BOOKING_4_HOURS_BEFORE, CONFIRM_BOOKING_LESS_24_HOURS, COORDINATE_VISIT, COORDINATE_VISIT_BOOKER, NOTIFY_ALLIANCE_WHATSAPP, SEND_CONFIRMATION_WHATSAPP, SEND_CONFIRMATION_WHATSAPP_WHEN_BOOKED, create_action_state, create_task_state, get_close_case_callback, get_create_task_callback


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
        get_create_task_callback(kind=CONFIRM_BOOKING_LESS_24_HOURS, sla={"hours": 24}, title="Confirmar visita 24 hrs antes")
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
    key=COORDINATE_VISIT_BOOKER,
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

    }
)

# State colocar rol asignado
state_cancelation_motive = create_action_state(
    key="cancelation_motive",
    name="Motivo de cancelación",
    flow=confirm_booking_48_hours_before,
    metadata={
        
    }
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
        get_create_task_callback(kind=CONFIRM_BOOKING_4_HOURS_BEFORE, sla={"hours": 48}, title="Confirmar visita 4hrs antes")
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